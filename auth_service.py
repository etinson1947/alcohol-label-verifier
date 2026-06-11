```python
import msal
import os


class AuthService:

    def __init__(self):

        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.tenant_id = os.getenv("TENANT_ID")

        self.authority = f"https://login.microsoftonline.com/{self.tenant_id}"

        self.app = msal.ConfidentialClientApplication(
            self.client_id,
            authority=self.authority,
            client_credential=self.client_secret
        )

    def get_token(self):

        result = self.app.acquire_token_for_client(
            scopes=["https://graph.microsoft.com/.default"]
        )

        return result.get("access_token")
```
