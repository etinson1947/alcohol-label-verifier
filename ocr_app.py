from flask import Flask, request, jsonify
from paddleocr import PaddleOCR

app = Flask(__name__)
ocr = PaddleOCR(use_angle_cls=True, lang="en")


@app.route("/ocr", methods=["POST"])
def run_ocr():

    file = request.files["file"]

    path = f"/tmp/{file.filename}"
    file.save(path)

    result = ocr.ocr(path)

    return jsonify(result)