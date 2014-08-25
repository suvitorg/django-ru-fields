# -*- coding: utf-8 -*
import logging

from django.forms import ValidationError
from django.forms.fields import Field, RegexField
from django.utils.encoding import smart_unicode, smart_str

from django_ru_fields.utils import test_inn, test_inn_org

logger = logging.getLogger(__name__)


class RUPostalCodeField(RegexField):
    default_error_messages = {
        'invalid': u'Введите верный почтовый индекс в формате XXXXXX.',
    }
    def __init__(self, *args, **kwargs):
        super(RUPostalCodeField, self).__init__(r'^\d{6}$', *args, **kwargs)


class RUKPPNumberField(RegexField):
    default_error_messages = {
        'invalid': u'Введите верный КПП в формате XXXXXXXXX.',
    }
    def __init__(self, *args, **kwargs):
        super(RUKPPNumberField, self).__init__(r'^\d{9}$', *args, **kwargs)


class RUINNNumberField(Field):
    """
    A form field that validates Russian INN numbers.
    """
    default_error_messages = {
        'invalid': u'Введите верный ИНН.',
    }

    def clean(self, value):
        value = super(RUINNNumberField, self).clean(value)
        if value == u'':
            return value
        try:
            inn_number = int(value)
        except ValueError:
            raise ValidationError(self.error_messages['invalid'])

        if not self.has_valid(value):
            raise ValidationError(self.error_messages['invalid'])

        return smart_unicode(value)

    def has_valid(self, value):
        return test_inn(value)


class RUINNOrgNumberField(RUINNNumberField):
    """
    A form field that validates Russian INN numbers for orgs.
    """
    def has_valid(self, value):
        return test_inn_org(value)


class RUBICNumberField(RegexField):
    default_error_messages = {
        'invalid': u'Введите верный БИК в формате XXXXXXXXX.',
    }
    def __init__(self, *args, **kwargs):
        super(RUBICNumberField, self).__init__(
            r'^\d{9}$', *args, **kwargs)


class RUBankAccountNumberField(RegexField):
    default_error_messages = {
        'invalid': u'Введите верный номер рассчетного счета'
                   u' в формате XXXXXXXXXXXXXXXXX.',
    }
    def __init__(self, *args, **kwargs):
        super(RUBankAccountNumberField, self).__init__(
            r'^\d{20}$', *args, **kwargs)


class RUBankCorrAccountNumberField(RegexField):
    default_error_messages = {
        'invalid': u'Введите верный номер корреспондентского счета'
                   u' в формате 301XXXXXXXXXXXXXX.',
    }
    def __init__(self, *args, **kwargs):
        super(RUBankCorrAccountNumberField, self).__init__(
            r'^301\d{17}$', *args, **kwargs)


class RUOGRNNumberField(RegexField):
    default_error_messages = {
        'invalid': u'Введите верный ОГРН в формате 13 или 15(для ИП) цифр.',
    }
    def __init__(self, *args, **kwargs):
        super(RUOGRNNumberField, self).__init__(r'^\d{13}(\d{2})?$', *args, **kwargs)


class RUPhoneNumberField(RegexField):
    default_error_messages = {
        'invalid': u'Введите верный номер телефона в формате 10 цифр без 8.',
    }
    def __init__(self, *args, **kwargs):
        super(RUPhoneNumberField, self).__init__(r'^\d{10}$', *args, **kwargs)

    def to_python(self, value):
        value = super(RUPhoneNumberField, self).to_python(value)
        value = smart_str(value)
        value = value.translate(None, ' -[{(\/)}]')
        if value.startswith('+7'):
            value = value[2:]
        if (value.startswith('7') or value.startswith('8')) and len(value) > 10:
            value = value[1:]
        return value


class RUPassportNumberField(RegexField):

    default_error_messages = {
        'invalid': u'Введите правильный номер паспорта в формате XXXX XXXXXX.',
    }
    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(RUPassportNumberField, self).__init__(r'^\d{4} \d{6}$',
            max_length, min_length, *args, **kwargs)

