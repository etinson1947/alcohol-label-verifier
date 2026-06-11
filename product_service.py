```python
from models import Product


class ProductService:

    def get_product(
        self,
        sku
    ):

        return (
            Product.query
            .filter_by(
                sku=sku
            )
            .first()
        )
```
