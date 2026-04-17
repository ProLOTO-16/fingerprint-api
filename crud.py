from database import cursor, conn

print("CRUD LOADED")


# 🟢 CREATE (POST)
def create_fingerprint(data):
    return {"msg": "Data received (DB disabled)"}


def get_fingerprints():
    return {"msg": "No DB connected"}
