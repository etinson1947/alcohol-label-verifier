```python
class BrandNameValidator:

    rule_name = "Brand Name"

    def validate(
        self,
        text,
        product
    ):

        passed = (
            product.brand_name.upper()
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
