from fastapi import FastAPI

app = FastAPI()


@app.get("/chateo")
def read_root():
    return {"respuesta": "Bien y tú ?"}