from database.database import get_connection


def add_patient(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO patients
    (name,age,gender,phone,email,symptoms,diseases,medicines)
    VALUES(?,?,?,?,?,?,?,?)
    """, (
        data["name"],
        data["age"],
        data["gender"],
        data["phone"],
        data["email"],
        data["symptoms"],
        data["diseases"],
        data["medicines"]
    ))

    conn.commit()
    conn.close()


def get_patients():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")

    rows = cursor.fetchall()

    conn.close()

    return rows