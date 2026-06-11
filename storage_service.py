```python
import os
from azure.storage.blob import BlobServiceClient


class StorageService:

    def __init__(self):

        conn = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        container = os.getenv("AZURE_STORAGE_CONTAINER")

        self.client = BlobServiceClient.from_connection_string(conn)
        self.container = self.client.get_container_client(container)

    def upload_file(self, file_path, blob_name):

        with open(file_path, "rb") as data:

            self.container.upload_blob(
                name=blob_name,
                data=data,
                overwrite=True
            )

        return f"uploaded:{blob_name}"
```
