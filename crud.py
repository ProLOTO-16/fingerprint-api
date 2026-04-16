from database import cursor, conn

print("CRUD LOADED")


# 🟢 CREATE (POST)
def create_fingerprint(data):
    try:
        query = """
        INSERT INTO fingerprint (name, user_id, role, finger_position, fingerprint_data, sg_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            data.name,
            data.user_id,
            data.role,
            data.finger_position,
            data.fingerprint_data,
            data.sg_id
        )

        cursor.execute(query, values)
        conn.commit()

        return {"message": "Inserted successfully"}

    except Exception as e:
        conn.rollback()   # 🔥 VERY IMPORTANT
        return {"error": str(e)}

def search_fingerprint(user_id=None, name=None):
    try:
        query = "SELECT * FROM fingerprint WHERE 1=1"
        values = []

        if user_id:
            query += " AND user_id = %s"
            values.append(user_id)

        if name:
            query += " AND name = %s"
            values.append(name)

        cursor.execute(query, tuple(values))
        rows = cursor.fetchall()

        result = []

        for row in rows:
            result.append({
                "id": row[0],
                "name": row[1],
                "user_id": row[2],
                "role": row[3],
                "finger_position": row[4],
                "fingerprint_data": row[5],
                "sg_id": row[6]
            })

        return result

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}


def update_fingerprint(user_id, data):
    try:
        query = """
        UPDATE fingerprint
        SET name = %s,
            role = %s,
            finger_position = %s,
            fingerprint_data = %s,
            sg_id = %s
        WHERE user_id = %s
        """

        values = (
            data.name,
            data.role,
            data.finger_position,
            data.fingerprint_data,
            data.sg_id,
            user_id
        )

        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount == 0:
            return {"message": "No record found"}

        return {"message": "Updated successfully"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

# 🟢 READ (GET)
def get_all_fingerprints():
    try:
        query = "SELECT * FROM fingerprint"
        cursor.execute(query)

        rows = cursor.fetchall()

        result = []

        for row in rows:
            # Safe conversion (no index error)
            data = {
                "id": row[0] if len(row) > 0 else None,
                "name": row[1] if len(row) > 1 else None,
                "user_id": row[2] if len(row) > 2 else None,
                "role": row[3] if len(row) > 3 else None,
                "finger_position": row[4] if len(row) > 4 else None,
                "fingerprint_data": row[5] if len(row) > 5 else None,
                "sg_id": row[6] if len(row) > 6 else None
            }

            result.append(data)

        return result

    except Exception as e:
        return {"error": str(e)}
