import sqlite3

def get_connection():
    conn = sqlite3.connect("healnet.db", check_same_thread=False)
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        phone TEXT,
        email TEXT,
        symptoms TEXT,
        diseases TEXT,
        medicines TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_patient(name, age, gender, phone, email, symptoms, diseases, medicines):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO patients
    (name, age, gender, phone, email, symptoms, diseases, medicines)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        age,
        gender,
        phone,
        email,
        symptoms,
        diseases,
        medicines
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