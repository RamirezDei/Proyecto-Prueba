from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Pedido, engine, Base
from pydantic import BaseModel

# Asegurarse de que las tablas existan al iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class PedidoSchema(BaseModel):
    producto: str
    cantidad: int

@app.get("/pedidos")
def listar_pedidos(db: Session = Depends(get_db)):
    # Equivalente a: SELECT * FROM pedidos;
    return db.query(Pedido).all()

@app.post("/pedidos")
def crear_pedido(p: PedidoSchema, db: Session = Depends(get_db)):
    nuevo_pedido = Pedido(producto=p.producto, cantidad=p.cantidad)
    db.add(nuevo_pedido)
    db.commit() # Guarda en la DB
    db.refresh(nuevo_pedido)
    return nuevo_pedido

# 3. ACTUALIZAR (PUT)
@app.put("/pedidos/{pedido_id}")
def actualizar_pedido(pedido_id: int, p_actualizado: PedidoSchema, db: Session = Depends(get_db)):
    # Buscamos el pedido en la DB por su ID
    pedido_db = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    
    if not pedido_db:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    
    # Actualizamos los campos
    pedido_db.producto = p_actualizado.producto
    pedido_db.cantidad = p_actualizado.cantidad
    
    db.commit() # Guardar cambios en Postgres
    db.refresh(pedido_db)
    return {"mensaje": "Pedido actualizado", "data": pedido_db}

# 4. ELIMINAR (DELETE)
@app.delete("/pedidos/{pedido_id}")
def eliminar_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido_db = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    
    if not pedido_db:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    
    db.delete(pedido_db) # Marcar para eliminar
    db.commit() # Ejecutar el DELETE en Postgres
    return {"mensaje": f"Pedido {pedido_id} eliminado con éxito"}