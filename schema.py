from pydantic import BaseModel

class Fingerprint(BaseModel):
    name: str
    user_id: int
    role: str
    finger_position: str
    fingerprint_data: str
    sg_id: str
