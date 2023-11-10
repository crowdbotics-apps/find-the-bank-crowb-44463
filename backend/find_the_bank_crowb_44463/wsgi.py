"""
WSGI config for find_the_bank_crowb_44463 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "find_the_bank_crowb_44463.settings"
)

application = get_wsgi_application()
