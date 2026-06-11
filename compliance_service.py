```python
from services.ocr_service import (
    OCRService
)

from verifier import (
    OCRNormalizer,
    TTBRulesEngine
)


class ComplianceService:

    def __init__(self):

        self.ocr = OCRService()

        self.rules_engine = (
            TTBRulesEngine()
        )

        self.review_threshold = (
            0.75
        )

    def verify_label(
        self,
        image_path,
        product
    ):

        ocr_result = (
            self.ocr.extract_text(
                image_path
            )
        )

        normalized_text = (
            OCRNormalizer
            .normalize(
                ocr_result["text"]
            )
        )

        findings = (
            self.rules_engine
            .validate(
                normalized_text,
                product
            )
        )

        errors = []

        warnings = []

        for item in findings:

            if (
                item["severity"]
                == "ERROR"
                and not item["passed"]
            ):

                errors.append(
                    item
                )

            if (
                item["severity"]
                == "WARNING"
                and not item["passed"]
            ):

                warnings.append(
                    item
                )

        manual_review = (
            ocr_result["confidence"]
            < self.review_threshold
        )

        status = "PASS"

        if len(errors) > 0:
            status = "FAIL"

        if manual_review:
            status = (
                "MANUAL_REVIEW"
            )

        return {

            "status":
                status,

            "ocr_confidence":
                round(
                    ocr_result[
                        "confidence"
                    ],
                    3
                ),

            "manual_review":
                manual_review,

            "findings":
                findings,

            "errors":
                errors,

            "warnings":
                warnings,

            "normalized_text":
                normalized_text
        }
```
