```python
class AlcoholContentValidator:

    rule_name = "Alcohol Content"

    def validate(
        self,
        text,
        product
    ):

        passed = (
            product.alcohol_content.upper()
            in text
        )

        return {

            "rule":
                self.rule_name,

            "passed":
                passed,

            "severity":
                "ERROR"
        }
```
