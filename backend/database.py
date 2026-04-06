from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Estructura: postgresql://usuario:contraseña@localhost/nombre_db
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:tu_password@localhost/pedidos1"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo de la Tabla
class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    producto = Column(String)
    cantidad = Column(Integer)

# Crear las tablas en Postgres
Base.metadata.create_all(bind=engine)