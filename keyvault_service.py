```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os


class KeyVaultService:

    def __init__(self):

        vault_url = os.getenv("AZURE_KEYVAULT_URL")

        credential = DefaultAzureCredential()

        self.client = SecretClient(
            vault_url=vault_url,
            credential=credential
        )

    def get_secret(self, name):

        return self.client.get_secret(name).value
```
