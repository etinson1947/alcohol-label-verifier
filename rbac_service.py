```python id="rbac1"
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, role):

        self.id = id
        self.role = role


def requires_role(role):

    def decorator(func):

        def wrapper(*args, **kwargs):

            # placeholder RBAC logic
            return func(*args, **kwargs)

        return wrapper

    return decorator
```
