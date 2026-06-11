```python
from rapidfuzz import fuzz


class GovernmentWarningValidator:

    rule_name = "Government Warning"

    def validate(self, text, product):

        expected = (product.government_warning or "").upper()

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
            "severity": "ERROR" if not passed else "PASS"
        }
```
