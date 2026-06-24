import sqlite3

DATABASE_NAME = "career.db"


def get_connection():
    return sqlite3.connect(
        DATABASE_NAME,
        check_same_thread=False
    )


def create_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analyses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        role TEXT,
        score INTEGER,
        skills TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_analysis(username, role, score, skills):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO analyses
        (
            username,
            role,
            score,
            skills
        )
        VALUES
        (
            ?,
            ?,
            ?,
            ?
        )
        """,
        (
            username,
            role,
            score,
            ", ".join(skills)
        )
    )

    conn.commit()
    conn.close()


def get_analysis_history(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM analyses
        WHERE username=?
        ORDER BY id DESC
        """,
        (username,)
    )

    data = cursor.fetchall()

    conn.close()

    return data