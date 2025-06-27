from fastapi import FastAPI
from routers import (
    actividad,
    auditoria,
    destinos,
    opinion,
    pais,
    reserva,
    tipo_actividad,
    usuarios
)

app = FastAPI()

# Rutas simples para test
@app.get("/")
def read_root():
    return {"message": "API running on Railway!"}

# Incluir tus routers
app.include_router(actividad.router)
app.include_router(auditoria.router)
app.include_router(destinos.router)
app.include_router(opinion.router)
app.include_router(pais.router)
app.include_router(reserva.router)
app.include_router(tipo_actividad.router)
app.include_router(usuarios.router)
