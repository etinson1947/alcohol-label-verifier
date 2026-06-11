import json
from services.ocr_service import OCRService
from services.compliance_service import ComplianceService

ocr = OCRService()
compliance = ComplianceService()


def process_message(msg):

    data = json.loads(str(msg))

    image_path = data["image_path"]
    product = data["product"]

    result = compliance.verify_label(
        image_path,
        product
    )

    return result