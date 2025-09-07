from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get('/')
def read_root():
    return FileResponse("templates/index.html")


@app.get("/surprise")
def surprise():
    return {"message":"YAHOODI DI PaN DI PHUDDI"}