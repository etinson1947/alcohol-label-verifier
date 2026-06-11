```python
class ProofValidator:

    rule_name = "Proof Statement"

    def validate(self, text, product):

        expected = (product.proof or "").upper()

        passed = expected in text if expected else True

        return {
            "rule": self.rule_name,
            "passed": passed,
            "severity": "ERROR"
        }
```
