import sqlite3

DB_NAME = "quiz.db"

def get_db_connection():
    """Crée une connexion à la base de données."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    """Crée les tables nécessaires dans la base de données."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS question (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre TEXT NOT NULL,
                texte,
                image,
                position INTEGER
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS answers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question_id INTEGER,
                answer_text TEXT NOT NULL,
                is_correct BOOLEAN,
                FOREIGN KEY (question_id) REFERENCES question (id)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS participations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        """)
        conn.commit()

def rebuild_database():
    """Supprime les tables existantes et recrée les tables nécessaires dans la base de données."""
    with get_db_connection() as conn:
        cursor = conn.cursor()

        # Supprimer les tables existantes (dans l'ordre pour respecter les contraintes de clé étrangère)
        cursor.execute("DROP TABLE IF EXISTS participations")
        cursor.execute("DROP TABLE IF EXISTS answers")
        cursor.execute("DROP TABLE IF EXISTS question")

        # Recréer les tables
        cursor.execute("""
            CREATE TABLE question (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre TEXT NOT NULL,
                texte TEXT,
                image TEXT,
                position INTEGER
            )
        """)

        cursor.execute("""
            CREATE TABLE answers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question_id INTEGER,
                answer_text TEXT NOT NULL,
                is_correct BOOLEAN,
                FOREIGN KEY (question_id) REFERENCES question (id)
            )
        """)

        cursor.execute("""
            CREATE TABLE participations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        """)

        conn.commit()
