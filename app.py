```python
import os
from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

from config import Config
from database import db

from services.ocr_service import OCRService
from services.product_service import ProductService
from services.compliance_service import ComplianceService

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["REPORT_FOLDER"], exist_ok=True)

ocr_service = OCRService()

product_service = ProductService()

compliance_service = ComplianceService()


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/health")
def health():

    return jsonify(
        {
            "status": "healthy"
        }
    )


@app.route(
    "/api/verify",
    methods=["POST"]
)
def verify_labels():

    files = request.files.getlist(
        "files"
    )

    sku = request.form.get("sku")

    if not files:

        return jsonify(
            {
                "error":
                    "No files uploaded"
            }
        ), 400

    product = (
        product_service
        .get_product(sku)
    )

    if not product:

        return jsonify(
            {
                "error":
                    "Unknown SKU"
            }
        ), 404

    results = []

    for file in files:

        try:

            path = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(path)

            result = (
                compliance_service
                .verify_label(
                    image_path=path,
                    product=product
                )
            )

            results.append(
                {
                    "filename":
                        file.filename,
                    "result":
                        result
                }
            )

        except Exception as ex:

            results.append(
                {
                    "filename":
                        file.filename,
                    "status":
                        "ERROR",
                    "message":
                        str(ex)
                }
            )

    return jsonify(results)


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(
        host="0.0.0.0",
        port=5000
    )
```
