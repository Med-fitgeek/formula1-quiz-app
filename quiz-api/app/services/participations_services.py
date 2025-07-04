import sqlite3
from app.models import get_db_connection

def calculate_score_and_save(player_name, answer_ids):
    """
    Calcule le score et enregistre la participation.
    :param player_name: Nom du joueur.
    :param answer_ids: Liste des IDs locaux (1-4) ou globaux.
    :return: Un dictionnaire contenant le score calculé et le nom du joueur.
    """
    try:
        score = 0
        with get_db_connection() as conn:
            conn.row_factory = sqlite3.Row  # Pour retourner des dictionnaires
            cursor = conn.cursor()

            # Détection du mode (local ou global)
            is_local_ids = all(1 <= id_ <= 4 for id_ in answer_ids)

            if is_local_ids:
                # Mode local : Mapper les IDs locaux vers des IDs globaux
                global_answer_ids = []
                for question_position, local_answer_id in enumerate(answer_ids, start=1):
                    cursor.execute("""
                        SELECT id
                        FROM answers
                        WHERE question_id = (
                            SELECT id
                            FROM question
                            WHERE position = ?
                        )
                        LIMIT 1 OFFSET ?
                    """, (question_position, local_answer_id - 1))
                    result = cursor.fetchone()
                    if result:
                        global_answer_ids.append(result["id"])
                    else:
                        raise Exception(f"Aucune réponse trouvée pour la position {question_position} et l'ID local {local_answer_id}")

                answer_ids = global_answer_ids  # Utiliser les IDs globaux pour le calcul

            # Calculer le score avec les IDs globaux
            for answer_id in answer_ids:
                cursor.execute("""
                    SELECT is_correct
                    FROM answers
                    WHERE id = ?
                """, (answer_id,))
                result = cursor.fetchone()

                if result and result["is_correct"]:  # Si la réponse est correcte
                    score += 1

            # Enregistrer la participation
            cursor.execute("""
                INSERT INTO participations (player_name, score)
                VALUES (?, ?)
            """, (player_name, score))
            conn.commit()

        return {"playerName": player_name, "score": score}

    except Exception as e:
        raise Exception(f"Erreur lors du calcul du score : {str(e)}")



def get_all_participations():
    """
    Récupère toutes les participations de la base de données.
    :return: Liste de participations.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, player_name, score
            FROM participations
        """)
        participations = cursor.fetchall()

        # Transformer les résultats en liste de dictionnaires
        return [
            {"id": row["id"], "playerName": row["player_name"], "score": row["score"]}
            for row in participations
        ]
    

def delete_all_participations():
    """
    Supprime toutes les participations de la base de données.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM participations")
        conn.commit()


def delete_participation_by_id(participation_id):
    """
    Supprime une participation spécifique par son ID.
    :param participation_id: ID de la participation à supprimer.
    :return: True si la suppression a réussi, False sinon.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM participations WHERE id = ?", (participation_id,))
        conn.commit()
        return cursor.rowcount > 0

