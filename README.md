django-ru-fields
================

l10n russian fields: postal code, phone, tax uin, bank account

[![Build Status](https://travis-ci.org/suvitorg/django-ru-fields.svg?branch=master)](https://travis-ci.org/suvitorg/django-ru-fields)


Install
-------------

``pip install django-ru-fields``

Fields
-------------

RUPostalCodeField
====================

russian postal code

RUINNNumberField
====================

russian inn number for pysical and uridical agents(tax uin)

RUINNOrgNumberField
====================

russian inn number only for organisations

RUKPPNumberField
====================

russian kpp number (state of filial)

RUBICNumberField
===================

russian bank id number

RUBankAccountNumberField
============================

russian account number

RUBankCorrAccountNumberField
=================================

russian account number in central bank

RUOGRNNumberField
========================

russian organisation id number

RUPhoneNumberField
====================

russian telephone number

Examples
-----------

```python
from django import forms
from django_ru_fields.fields import RUKPPNumberField

class OrderForm(forms.Form):
    postal_code = RUPostalCodeField()
    inn = RUINNNumberField()
    kpp = RUKPPNumberField()

    bik = RUBICNumberField()
    account = RUBankAccountNumberField()

    phone = RUPhoneNumberField()
```

