import jwt
import datetime
from werkzeug.exceptions import Unauthorized


class JwtError(Exception):
    """Exception raised for jwt errors in the quiz app 
    """

    def __init__(self, message="Jwt error"):
        self.message = message
        super().__init__(self.message)


secret = "Groupe Henri Victor"
expiration_in_seconds = 3600


def build_token():
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expiration_in_seconds),
            'iat': datetime.datetime.utcnow(),
            'sub': 'quiz-app-admin'
        }
        # Convertir le token en chaîne UTF-8
        token = jwt.encode(
            payload,
            secret,
            algorithm="HS256"
        )
        return token
    except Exception as e:
        return str(e)  # Retourner l'exception sous forme de chaîne


def decode_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, secret, algorithms="HS256")
        # if decoding did not fail, this means we are correctly logged in
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise JwtError('Signature expired. Please log in again.')
    except jwt.InvalidTokenError as e:
        raise JwtError('Invalid token. Please log in again.')
