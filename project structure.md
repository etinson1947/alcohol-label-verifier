alcohol-label-verifier/

├── app.py
├── config.py
├── database.py
├── models.py
├── verifier.py

|\_\_ websocketapp.py (can be used for websocket integration)
│
├── services/
│   ├── ocr\_service.py
│   ├── compliance\_service.py
│   ├── storage\_service.py
│   └── product\_service.py

|   |\_\_ rbac\_service.py

|   |\_\_ pdf\_report\_service.py

|   |\_\_ queue\_service.py

|   |\_\_ socket\_service.py
│ 
├── validators/
│   ├── brand\_validator.py
│   ├── class\_validator.py
│   ├── alcohol\_validator.py
│   ├── proof\_validator.py
│   ├── net\_contents\_validator.py
│   ├── warning\_validator.py
│   └── bottler\_validator.py
│
├── templates/
│   ├── index.html
│   ├── results.html
│   └── review.html

|

|\_\_ frontend/

|   |\_\_ src/

|       |\_\_ app.js
│
├── static/
│
├── uploads/
├── reports/
├── logs/
│
├── migrations/

|   |\_\_	env.py

|       |\_\_ versions/

|             |\_\_ 001\_initial.py
│
├── deployment/
│   ├── Dockerfile
│   ├── startup.sh
│   ├── nginx.conf
│   ├── web.config
│   └── azure\_pipelines.yaml

|   |\_\_	main.bicep

|   |\_\_ aks-deployment.yaml

|   |\_\_ aks-service.yaml

|

|

|\_\_ .GitHub/

|   |\_\_ workflows/

|       |\_\_ deploy.yml

|       |\_\_ security-ci.yml

|

|\_\_ auth/

|   |\_\_ entra\_auth.py

|

|\_\_ workers/

|   |\_\_ ocr\_worker.py

|

|\_\_ docker/

|   |\_\_ ocr-service/

|       |\_\_ ocr\_app.py (can be used scalable architecture)

|

|\_\_ audit/

|   |\_\_ immutable\_log.py

|

|\_\_ compliance/

|   |\_\_ ttb\_rules.py

|

|\_\_ ai/

|   |\_\_ anomaly\_detector.py

|   |\_\_ counterfeit\_model.py

|

|\_\_ architecture/

|   |\_\_ federated\_deployment.yaml

|

|\_\_ helm/

|   |\_\_ alcohol-verifier/

|       |\_\_ values.yaml

|          |\_\_ templates/

|             |\_\_ deployment.yaml

|

|\_\_ compliance/

|   |\_\_ nist\_controls.py

|   |\_\_ evidence\_engine.py

|
│
└── tests/

