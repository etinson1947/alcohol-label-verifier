```python
class ClassTypeValidator:

    rule_name = "Class Type"

    def validate(
        self,
        text,
        product
    ):

        passed = (
            product.class_type.upper()
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
