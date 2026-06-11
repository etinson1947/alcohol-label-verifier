```bash
#!/bin/bash

gunicorn \
--bind=0.0.0.0:${PORT:-8000} \
--workers 4 \
--threads 4 \
--timeout 300 \
app:app
```
