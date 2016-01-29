from Sense.settings.default import *

DEBUG = False

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SenseDB',
        'USER': 'mraaa711128',
        'PASSWORD': 'Fdax82248379',
        'HOST': 'sensedb.cmy0gstkq343.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}
