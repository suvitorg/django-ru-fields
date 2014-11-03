import sys
from django.conf import settings
from django.core.management import call_command

settings.configure(
    INSTALLED_APPS=[
        #'django.contrib.auth',
        #'django.contrib.contenttypes',
        #'django.contrib.sessions',
        #'django.contrib.admin',
        'django_ru_fields',
    ],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    },
)

call_command("test", "django_ru_fields")
sys.exit(0)
