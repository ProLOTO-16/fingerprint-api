from fastapi import FastAPI
from schema import Fingerprint
from typing import Optional
import crud
import os




app = FastAPI()


@app.post("/fingerprint/")
def create_fingerprint(data: Fingerprint):
    return crud.create_fingerprint(data)


@app.get("/fingerprints/")
def get_fingerprints():
    try:
        data = crud.get_all_fingerprints()
        return {"data": data}
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/fingerprint/search")
def search_fingerprint(user_id: Optional[int] = None, name: Optional[str] = None):
    return {"data": crud.search_fingerprint(user_id, name)}


@app.put("/fingerprint/{user_id}")
def update_fingerprint(user_id: int, data: Fingerprint):
    return crud.update_fingerprint(user_id, data)

@app.get("/test-env")
def test_env():
    return {
        "DB_NAME": os.getenv("DB_NAME"),
        "DB_USER": os.getenv("DB_USER"),
        "DB_HOST": os.getenv("DB_HOST"),
        "DB_PORT": os.getenv("DB_PORT")
    }





