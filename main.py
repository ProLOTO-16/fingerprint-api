from fastapi import FastAPI
from schema import Fingerprint
from typing import Optional
import crud

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




