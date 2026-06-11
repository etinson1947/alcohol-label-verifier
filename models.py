from database import db

class Product(db.Model):

```
__tablename__ = "products"

sku = db.Column(
    db.String(50),
    primary_key=True
)

brand_name = db.Column(
    db.String(255),
    nullable=False
)

class_type = db.Column(
    db.String(255),
    nullable=False
)

alcohol_content = db.Column(
    db.String(100),
    nullable=False
)

proof = db.Column(
    db.String(100)
)

net_contents = db.Column(
    db.String(100)
)

government_warning = db.Column(
    db.Text
)

bottler_name = db.Column(
    db.String(255)
)

bottler_address = db.Column(
    db.String(255)
)
```

class ComplianceResult(db.Model):

```
__tablename__ = "compliance_results"

id = db.Column(
    db.Integer,
    primary_key=True
)

filename = db.Column(
    db.String(255)
)

sku = db.Column(
    db.String(50)
)

status = db.Column(
    db.String(50)
)

ocr_confidence = db.Column(
    db.Float
)

findings = db.Column(
    db.JSON
)

created_date = db.Column(
    db.DateTime,
    server_default=db.func.now()
)
```
