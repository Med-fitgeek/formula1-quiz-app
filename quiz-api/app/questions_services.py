from app.models import get_db_connection

def add_question_to_db(title, text, image, position, possible_answers):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Insérer la question dans la base
        cursor.execute("""
            INSERT INTO question (titre, texte, image, position)
            VALUES (?, ?, ?, ?)
        """, (title, text, image, position))
        question_id = cursor.lastrowid

        # Insérer les réponses
        for answer in possible_answers:
            cursor.execute("""
                INSERT INTO answers (question_id, answer_text, is_correct)
                VALUES (?, ?, ?)
            """, (question_id, answer['text'], answer['isCorrect']))

        conn.commit()
        conn.close()

        return question_id
    except Exception as e:
        raise Exception(f"Error in adding question: {str(e)}")

def delete_question_from_db(question_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Supprimer la question et ses réponses associées
        cursor.execute("DELETE FROM answers WHERE question_id = ?", (question_id,))
        cursor.execute("DELETE FROM question WHERE id = ?", (question_id,))

        # Réinitialiser le compteur d'auto-incrémentation pour la table question
        cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'question'")

        conn.commit()
        conn.close()
    except Exception as e:
        raise Exception(f"Error in deleting question: {str(e)}")

def delete_all_questions_from_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Supprimer toutes les réponses et toutes les questions
        cursor.execute("DELETE FROM answers")
        cursor.execute("DELETE FROM question")

        # Réinitialiser le compteur d'auto-incrémentation pour la table question
        cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'question'")

        conn.commit()
        conn.close()
    except Exception as e:
        raise Exception(f"Error in deleting all questions: {str(e)}")
