from .base import *

DEBUG = True

#Database Config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#Overrider Development
INSTALLED_APPS += [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig'
]