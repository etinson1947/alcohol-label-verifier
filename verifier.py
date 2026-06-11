```python
import re

from validators.brand_validator import (
    BrandNameValidator
)

from validators.class_validator import (
    ClassTypeValidator
)

from validators.alcohol_validator import (
    AlcoholContentValidator
)

from validators.proof_validator import (
    ProofValidator
)

from validators.net_contents_validator import (
    NetContentsValidator
)

from validators.warning_validator import (
    GovernmentWarningValidator
)

from validators.bottler_validator import (
    BottlerValidator
)


class OCRNormalizer:

    @staticmethod
    def normalize(text):

        text = text.upper()

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        text = text.replace(
            "ALC VOL",
            "ALC./VOL."
        )

        text = text.replace(
            "ALC/VOL",
            "ALC./VOL."
        )

        return text


class TTBRulesEngine:

    def __init__(self):

        self.validators = [

            BrandNameValidator(),

            ClassTypeValidator(),

            AlcoholContentValidator(),

            ProofValidator(),

            NetContentsValidator(),

            GovernmentWarningValidator(),

            BottlerValidator()
        ]

    def validate(
        self,
        text,
        product
    ):

        results = []

        for validator in self.validators:

            results.append(
                validator.validate(
                    text,
                    product
                )
            )

        return results
```
