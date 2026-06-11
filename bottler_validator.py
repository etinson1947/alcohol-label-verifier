```python
from rapidfuzz import fuzz


class BottlerValidator:

    rule_name = "Bottler Information"

    def validate(self, text, product):

        expected = (product.bottler_name or "").upper()

        if not expected:
            return {
                "rule": self.rule_name,
                "passed": True,
                "severity": "WARNING"
            }

        score = fuzz.partial_ratio(expected, text)

        passed = score >= 90

        return {
            "rule": self.rule_name,
            "passed": passed,
            "score": score,
            "severity": "WARNING"
        }
```
