""" "Валідатор електронної пошти"

1. Створіть регулярний вираз для валідації адрес електронної пошти.
2. Створіть тести для перевірки вашого регулярного виразу.
Файл з валідними та невалідними електронними адресами додається.
"""

import json
import re

EMAIL_VALIDATE_REGEX = r"^[\+\w\.-]+@([a-zA-Z\d][a-zA-Z\d-]+\.)+[a-zA-z]{2,4}$"
EMAIL_VALIDATOR = re.compile(EMAIL_VALIDATE_REGEX)

with open("emails.json") as f:
    emails = json.load(f)

valid_emails = emails["valid_emails"]
invalid_emails = emails["invalid_emails"]

for email in valid_emails:
    assert EMAIL_VALIDATOR.fullmatch(email)

for email in invalid_emails:
    assert not EMAIL_VALIDATOR.fullmatch(email)
