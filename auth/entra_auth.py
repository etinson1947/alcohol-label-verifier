import os
from flask import redirect, request, session, url_for
import msal


class EntraAuth:

    def __init__(self):

        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.tenant_id = os.getenv("TENANT_ID")

        self.authority = (
            f"https://login.microsoftonline.com/{self.tenant_id}"
        )

        self.app = msal.ConfidentialClientApplication(
            self.client_id,
            authority=self.authority,
            client_credential=self.client_secret
        )

    def login_url(self):

        return self.app.get_authorization_request_url(
            scopes=["User.Read"],
            redirect_uri=os.getenv("REDIRECT_URI")
        )

    def callback(self, code):

        result = self.app.acquire_token_by_authorization_code(
            code,
            scopes=["User.Read"],
            redirect_uri=os.getenv("REDIRECT_URI")
        )

        session["user"] = result.get("id_token_claims")

        return result
