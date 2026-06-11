```python
class NetContentsValidator:

    rule_name = "Net Contents"

    def validate(self, text, product):

        expected = (product.net_contents or "").upper()

        passed = expected in text if expected else True

        return {
            "rule": self.rule_name,
            "passed": passed,
            "severity": "ERROR"
        }
```
