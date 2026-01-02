import psycopg2, os

def init_progreso():
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS progreso_tema (
        tema TEXT PRIMARY KEY,
        respondidas INTEGER DEFAULT 0,
        aciertos INTEGER DEFAULT 0,
        ultima_actualizacion TIMESTAMP DEFAULT now()
    );
    """)
    conn.commit()
    conn.close()
    print("✅ Tabla progreso_tema OK")
