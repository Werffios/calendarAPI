from fastapi import FastAPI, HTTPException
import datetime
import holidays

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Nuevo endpoint para verificar si una fecha es festiva en Colombia.
@app.get("/festivo/{fecha}")
async def verificar_festivo(fecha: str):
    """
    Recibe una fecha en formato yyyy-mm-dd y retorna:
    - 'festivo': true/false (si es festivo)
    - 'nombre_festivo': el nombre del festivo (si la fecha es festiva)
    """
    try:
        fecha_dt = datetime.datetime.strptime(fecha, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Fecha inválida. Formato debe ser yyyy-mm-dd")

    # Usamos la librería holidays para obtener los festivos de Colombia para el año de la fecha.
    colombia_holidays = holidays.Colombia(years=fecha_dt.year)
    es_festivo = fecha_dt in colombia_holidays

    return {
        "fecha": fecha,
        "festivo": es_festivo,
        "nombre_festivo": colombia_holidays.get(fecha_dt) if es_festivo else None
    }
