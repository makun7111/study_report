from .settings_common import*
SECRET_KEY = 'django-insecure-bt(00h8k#9a3e%ya%1zu=n6$ljlqp8$w5@g7_ubo@agd0!-1vr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

LOGGING={
    'version':1,
    'disable_existing_loggers':False,

    'loggers':{
        'django':{
        'handlers':['console'],
        'level':'INFO',
        },
        'diary':{
            'handlers':['console'],
            'level':'DEBUG',
        },

    },

    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev'
        },
    },

    'formatters':{
        'dev':{
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT=os.path.join(BASE_DIR,'media')