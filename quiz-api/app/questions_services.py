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
    
    
def get_all_questions_from_db():
    """
    Récupère toutes les questions avec leurs réponses associées.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Récupérer toutes les questions
        cursor.execute("SELECT * FROM question")
        questions = cursor.fetchall()

        result = []
        for question in questions:
            cursor.execute("""
                SELECT id, answer_text, is_correct
                FROM answers
                WHERE question_id = ?
            """, (question['id'],))
            answers = cursor.fetchall()

            result.append({
                "id": question['id'],
                "title": question['titre'],
                "text": question['texte'],
                "image": question['image'],
                "position": question['position'],
                "possibleAnswers": [
                    {"id": answer['id'], "text": answer['answer_text'], "isCorrect": answer['is_correct']}
                    for answer in answers
                ]
            })

        conn.close()
        return result

    except Exception as e:
        raise Exception(f"Error in fetching all questions: {str(e)}")


def get_question_by_position_from_db(position):
    """
    Récupère une question par position avec ses réponses associées.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Récupérer la question par position
        cursor.execute("SELECT * FROM question WHERE position = ?", (position,))
        question = cursor.fetchone()

        if not question:
            raise Exception(f"Question avec la position {position} non trouvée")

        # Récupérer les réponses associées à la question
        cursor.execute("""
            SELECT id, answer_text, is_correct
            FROM answers
            WHERE question_id = ?
        """, (question['id'],))  # Utilisation correcte de question['id']
        answers = cursor.fetchall()

        conn.close()
        # Construire la réponse
        return {
            "id": question["id"],
            "title": question["titre"],
            "text": question["texte"],
            "image": question["image"],
            "position": question["position"],
            "possibleAnswers": [
                {"id": answer["id"], "text": answer["answer_text"], "isCorrect": answer["is_correct"]}
                for answer in answers
            ]
        }

    except Exception as e:
        raise Exception(f"Error in fetching question by position: {str(e)}")





def update_question_in_db(question_id, title, text, image, position, possible_answers):
    """
    Met à jour une question et ses réponses associées.
    :param question_id: ID de la question à mettre à jour.
    :param title: Nouveau titre de la question.
    :param text: Nouveau texte de la question.
    :param image: Nouvelle image de la question.
    :param position: Nouvelle position de la question.
    :param possible_answers: Liste des réponses associées.
    :return: True si la mise à jour a réussi, False sinon.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Vérifier si la question existe
        cursor.execute("SELECT * FROM question WHERE id = ?", (question_id,))
        question = cursor.fetchone()
        if not question:
            raise Exception(f"Question avec l'ID {question_id} non trouvée")

        # Mettre à jour la question
        cursor.execute("""
            UPDATE question
            SET titre = ?, texte = ?, image = ?, position = ?
            WHERE id = ?
        """, (title, text, image, position, question_id))

        # Supprimer les anciennes réponses associées
        cursor.execute("DELETE FROM answers WHERE question_id = ?", (question_id,))

        # Ajouter les nouvelles réponses
        for answer in possible_answers:
            cursor.execute("""
                INSERT INTO answers (question_id, answer_text, is_correct)
                VALUES (?, ?, ?)
            """, (question_id, answer['text'], answer['isCorrect']))

        conn.commit()
        conn.close()
        return True

    except Exception as e:
        raise Exception(f"Error in updating question: {str(e)}")



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
