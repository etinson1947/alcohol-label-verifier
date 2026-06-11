```python id="pdf1"
from reportlab.pdfgen import canvas
import os


class PDFReportService:

    def generate(self, output_path, data):

        c = canvas.Canvas(output_path)

        c.drawString(100, 800, "Alcohol Label Compliance Report")

        y = 750

        for item in data.get("findings", []):

            c.drawString(100, y, f"{item['rule']}: {item['passed']}")
            y -= 20

        c.save()

        return output_path
```
