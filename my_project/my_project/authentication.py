import os

import firebase_admin
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from firebase_admin import auth
from firebase_admin import credentials
from rest_framework import authentication
from rest_framework import exceptions

from .exceptions import FirebaseError
from .exceptions import NoAuthToken
from .exceptions import InvalidAuthToken

cred = credentials.Certificate(
    {
        "type": "service_account",
        "project_id": "python-training-f5082",
        "private_key_id": "3ac8bb03ee3e75d5e018ee4b875d7e442882d419",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDKkuVCdcGRM7Ls\n2XhpMuX72s81Q7iUUzes/oEDXvFUU0WYxFPpxIM1QR+rOAb82YcDH9VpGKGheTg7\nczlVgdeMuAg7X9S4ZvbrY77Jmxykoq50mroubqrK1wh6iLiMxk+rGcTCGYLnDPgV\n3jlSNzFShhfKZcC24I78+sv1NQPuVUbpJqang0bEX8e2XaXHo6w9A4OruHJq2AzG\nWGE3zZiH41Ltk1RjgF5oUcTmhMugeIYwAI+As8+N1TfS3UaqAjQm4qTHVtjcJg6v\n2uYpLkqwOTlu5QbUm5iUv//T0WTDw6QFxmdRGKRHnVtlsv+htzZ1a/GJKWROS7WE\nUsXutBenAgMBAAECggEABfQHNMrNI31Hdtp1RXIvfBVUHZad6A4CBt174SN7KCVC\nWFj8tlQGHxyI17lPy0KBS0A2P15v8ZTkaCrctnyYXxRReZ05XSn5e7V0t+wNDXGS\neu7JJfAuqMNlBmTaN5jkYnzhYWrqg+vHpqzfNmFU274BGPugjD9RNHISaGRkdy6R\nAOfacMxXKpgAeH3s9dTKVAwYK1RL5un8NaIWSGjbpflcN8An4MrOz80CbkJCYwD7\nRvmE8qYR8qi6yx/GfZraH15XN44cmT4KaCJ4GrhTefqV4oTggfYE5WIFjhXrdc1B\nxpLqNnsiqI8dNMmEs/LG9xGmPxdHagqGvkAbRYBaEQKBgQDqerio4EYtX1ZIQuef\n7g6BIc5QxvgENPQbbodAou29MManWGu/4gL9xcDfmM43QE6dS7AWits8ecYzgZE4\nCbO5ziOiWNFn/GJRXDxkaIG7laXLCve0e7dQlLBnNX7oChBoMD1XrjqpC6HvFCW2\nPZn8tnaXO4shs5o+h3WVdqnK7QKBgQDdKocRGQMm1ABRZVGtF9JKGQZiBetVD6AB\nWAsXNhXQVJXdrY/WTp+5E9X7dxeGHlIDezQJ0Y6XxDfDNQr6gUqGz8dwPF4Tpspu\nnavEUcNlD6sb1ZqCnjRzJSftq/Mcy66BPWKtF2PPrYY4fmHB4rieQJrLL2BA1XNr\nuCpYZXtWYwKBgDH21pR9vdZ7QzqArzSgGI0htAH4c+8JjZ6uzblTPo+a7inIqKUp\ntvN2iSPcPsz9MgNIlownKJJZbIebK2OihZ6pM2SrwmuDFzw5CFFpB4P+XmbGvoPB\n/Qz5siE7///X7SkWZmvhn3RYGziDtYmA1OhJxTlyobIbwFlkqgSgVYv9AoGBAIjh\nVkDVuyaf1SaLT5aShLsJa/Lk+PZnOj86r3qJJc0PXMWbMsePV7ljNm9xEKUYROgU\nq2tcQCVb8qslPAs4U9jF5ghnxE3jT6xQd0uE0yrMHLmYZQ1sPsf4+hJV9pwez3z7\ncgPw0vxoyAZU6cnmuR5wm50fUDIwKURE8ihNfp1DAoGAGgkqw5nnRSiUM13dur+l\n5yuRPvvPccwaKspkUjbAZOUzhkU9OCi57gfMAcm13HAPIYhHD0htaTcCvPRv03P/\nYlsH1geIYaR13msj1vqP7GPfzj/yhiG+qujum2yx993dda1lA2UZnnSO+tZ+2yYM\n2OjcOp5+elZHrWCcvfMTBqw=\n-----END PRIVATE KEY-----\n".replace("\\n", "\n"),
        "client_email": "firebase-adminsdk-s0516@python-training-f5082.iam.gserviceaccount.com",
        "client_id": "109781028870357660132",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-s0516%40python-training-f5082.iam.gserviceaccount.com"
    }
)

default_app = firebase_admin.initialize_app(cred)


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")
            pass

        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()

        user, created = User.objects.get_or_create(username=uid)
        #user.profile.last_activity = timezone.localtime()

        return (user, None)