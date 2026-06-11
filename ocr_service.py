```python
import cv2

from paddleocr import PaddleOCR


class OCRService:

    def __init__(self):

        self.ocr = PaddleOCR(
            use_angle_cls=True,
            lang="en"
        )

    def preprocess_image(
        self,
        image_path
    ):

        image = cv2.imread(
            image_path
        )

        if image is None:

            raise Exception(
                "Unable to load image"
            )

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        blur = cv2.GaussianBlur(
            gray,
            (3, 3),
            0
        )

        threshold = (
            cv2.adaptiveThreshold(
                blur,
                255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,
                11,
                2
            )
        )

        return threshold

    def extract_text(
        self,
        image_path
    ):

        image = (
            self.preprocess_image(
                image_path
            )
        )

        results = self.ocr.ocr(
            image
        )

        lines = []

        confidence_scores = []

        for page in results:

            if page is None:
                continue

            for item in page:

                text = item[1][0]

                confidence = (
                    item[1][1]
                )

                lines.append(
                    text
                )

                confidence_scores.append(
                    confidence
                )

        if len(lines) == 0:

            raise Exception(
                "No text detected"
            )

        avg_confidence = (
            sum(confidence_scores)
            / len(confidence_scores)
        )

        return {

            "text":
                "\n".join(lines),

            "confidence":
                avg_confidence
        }
```
