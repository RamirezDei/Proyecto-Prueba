from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Tarea(BaseModel):
    id: int
    titulo: str

# Simulación de Base de Datos
db = [
    {"id": 1, "titulo": "Estudiar Laravel"},
    {"id": 2, "titulo": "Probar FastAPI"}
]

# 1. LEER (GET)
@app.get("/tareas", response_model=List[Tarea])
def obtener_tareas():
    return db

# 2. CREAR (POST)
@app.post("/tareas")
def crear_tarea(tarea: Tarea):
    db.append(tarea.dict())
    return {"mensaje": "Tarea creada"}

# 3. ACTUALIZAR (PUT)
@app.put("/tareas/{tarea_id}")
def actualizar_tarea(tarea_id: int, tarea_actualizada: Tarea):
    for index, t in enumerate(db):
        if t["id"] == tarea_id:
            db[index] = tarea_actualizada.dict()
            return {"mensaje": "Tarea actualizada"}
    raise HTTPException(status_code=404, detail="No encontrada")

# 4. ELIMINAR (DELETE)
@app.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int):
    for index, t in enumerate(db):
        if t["id"] == tarea_id:
            db.pop(index)
            return {"mensaje": "Tarea eliminada"}
    raise HTTPException(status_code=404, detail="No encontrada")