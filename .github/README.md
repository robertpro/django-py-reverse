# django-py-reverse

> 

[![Latest Version on PyPI](https://img.shields.io/pypi/v/django_py_reverse.svg)](https://pypi.python.org/pypi/django_py_reverse/)
[![Supported Implementations](https://img.shields.io/pypi/pyversions/django_py_reverse.svg)](https://pypi.python.org/pypi/django_py_reverse/)
![Build Status](https://github.com/robertpro/django-py-reverse/actions/workflows/test.yaml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/https://github.com/robertpro/django-py-reverse/badge.svg?branch=master)](https://coveralls.io/github/https://github.com/robertpro/django-py-reverse?branch=master)
[![Built with PyPi Template](https://img.shields.io/badge/PyPi_Template-v0.6.1-blue.svg)](https://github.com/christophevg/pypi-template)


## Installation

```bash
pip install django_py_reverse

# or using poetry
poetry add django_py_reverse
```

## Usage

```python
from django_py_reverse import Urls

API_ENDPOINT = "https://example.com/api/v1"
data_urls = {
    "urls": [
        [
            "account_confirm_email",
            [["accounts/confirm_email/%(key)s/", ["key"]]],
        ],
        ["account_delete", [["accounts/delete/", []]]],
        ["account_password_reset", [["es/accounts/password/reset/", []]]],
        [
            "account_password_reset_token",
            [
                [
                    "accounts/password/reset/%(uidb36)s-%(token)s/",
                    ["uidb36", "token"],
                ]
            ],
        ],
    ],
    "prefix": "/",
}

urls = Urls(data=data_urls, url_prefix=API_ENDPOINT).factory()

print(urls['account_confirm_email'](key="123"))
print(urls['account_delete']())
print(urls['account_password_reset']())
print(urls['account_password_reset_token'](uidb36="123", token="456"))

# Output:
# https://example.com/api/v1/accounts/confirm_email/123/
# https://example.com/api/v1/accounts/delete/
# https://example.com/api/v1/es/accounts/password/reset/
# https://example.com/api/v1/accounts/password/reset/123-456/
```

### Include JS Style

```python
urls = Urls(data=data_urls, url_prefix=API_ENDPOINT, include_js_style=True).factory()

print(urls['accountConfirmEmail'](key="123"))
print(urls['accountDelete']())
print(urls['accountPasswordReset']())
print(urls['accountPasswordResetToken'](uidb36="123", token="456"))

# Output:
# https://example.com/api/v1/accounts/confirm_email/123/
# https://example.com/api/v1/accounts/delete/
# https://example.com/api/v1/es/accounts/password/reset/
# https://example.com/api/v1/accounts/password/reset/123-456/
```
