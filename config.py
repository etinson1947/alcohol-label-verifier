import os
from dotenv import load_dotenv

load_dotenv()

class Config:

```
SECRET_KEY = os.getenv(
    "SECRET_KEY"
)

SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False

OCR_CONFIDENCE_THRESHOLD = float(
    os.getenv(
        "OCR_CONFIDENCE_THRESHOLD",
        "0.75"
    )
)

UPLOAD_FOLDER = os.getenv(
    "UPLOAD_FOLDER",
    "uploads"
)

REPORT_FOLDER = os.getenv(
    "REPORT_FOLDER",
    "reports"
)

AZURE_STORAGE_CONNECTION_STRING = os.getenv(
    "AZURE_STORAGE_CONNECTION_STRING"
)

AZURE_STORAGE_CONTAINER = os.getenv(
    "AZURE_STORAGE_CONTAINER"
)

AZURE_KEYVAULT_URL = os.getenv(
    "AZURE_KEYVAULT_URL"
)
```
