```python
from applicationinsights import TelemetryClient
import os


class MonitoringService:

    def __init__(self):

        key = os.getenv("APPINSIGHTS_INSTRUMENTATIONKEY")

        self.client = TelemetryClient(key)

    def log_event(self, name, properties=None):

        self.client.track_event(name, properties or {})

    def log_exception(self, exception):

        self.client.track_exception()
```
