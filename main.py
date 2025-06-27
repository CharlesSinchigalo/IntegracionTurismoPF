from fastapi import FastAPI
from database import Base, engine

# Importar modelos (necesario si luego quieres usarlo en routers)
import models.usuario
import models.pais
import models.destino
import models.tipo_actividad
import models.actividad
import models.opinion
import models.reserva
import models.auditoria

# Importar routers
from routers import usuarios
from routers import pais
from routers import destinos
from routers import tipo_actividad
from routers import actividad
from routers import opinion
from routers import reserva
from routers import auditoria

# Importar autenticación (Google OAuth)
from auth import google_oauth as auth

# Crear la app FastAPI
app = FastAPI(
    title="API Turismo",
    description="Backend para gestión de turismo, actividades y reservas.",
    version="1.0.0"
)

# ✅ ESTA LÍNEA CREA LAS TABLAS
Base.metadata.create_all(bind=engine)

# Rutas base
@app.get("/")
def read_root():
    return {"msg": "API de Turismo funcionando"}

# Registrar routers
app.include_router(usuarios.router)
app.include_router(auth.router)
app.include_router(pais.router)
app.include_router(destinos.router)
app.include_router(tipo_actividad.router)
app.include_router(actividad.router)
app.include_router(opinion.router)
app.include_router(reserva.router)
app.include_router(auditoria.router)
