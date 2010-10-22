from unipath import Path

APP_ROOT = Path(__file__, '..')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': APP_ROOT + 'social_links.db',
        'TEST_NAME': ':memory:',
    }
}

INSTALLED_APPS = (
    'social_links',
)
