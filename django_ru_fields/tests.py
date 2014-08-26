# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.exceptions import ValidationError

from django_ru_fields.forms import RUPhoneNumberField



class TestRuPhoneField(TestCase):

    def setUp(self):
        self.bad_phones = ['+7 (343) 213-93-022222',
                           '+7892210900123',
                           ]
        self.good_phones = [('+7 (343) 213-93-02', '3432139302'),
                            ('+79221090012', '9221090012'),
                            ('8-922-109-00-12', '9221090012'),
                            ('(+7) {922}- 109 0012', '9221090012'),
                            ('+789221090012', '9221090012'),
                            ('79221090012', '9221090012'),
                           ]

    def test(self):
        for bad_phone in self.bad_phones:
            self.assertRaises(ValidationError,
                              RUPhoneNumberField().clean,
                              bad_phone)

        for test_phone, good_phone in self.good_phones:
            self.assertEqual(good_phone,
                             RUPhoneNumberField().clean(test_phone))
