from .settings_common import *
#本番運用環境用にセキュリティキーを生成し環境変数から読み込む
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
AWS_SES_REGION_NAME = 'us-east-1'
AWS_SES_REGION_ENDPOINT = 'email.us-east-1.amazonaws.com'
# デバッグモードを有効にするかどうか (本番運用では必ずFalseにする)
DEBUG = True
# 許可するホスト名のリスト
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]
# 静的ファイルを配置する場所
STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'
 #Amazon SES関連設定
AWS_ACCESS_KEY_ID = 'AKIA56Y4XT7SDVPWWEWB'
AWS_SECRET_ACCESS_KEY = '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'
EMAIL_BACKEND = 'django_ses.SESBackend'
#3 ロギング
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'django': {
            'handlers':['file'],
            'level':'INFO',
        },

# diaryアプリケーションが利用するロガー
            'diary': {
                'handlers': ['file'],
                'level': 'INFO',
            },
        },
#23 ハンドラの設定
            'handlers': {
                'file': {
                    'level': 'INFO',
                    'class': 'logging.handlers.TimedRotatingFileHandler',
                    'filename': os.path.join(BASE_DIR,'logs/django.log'),
                    'formatter': 'prod',
                    'when': 'D', # ログローテーション(新しいロ ファイルへの切り替え)間隔の単位(D=日)
                    'interval': 1, # ログローテーション間隔(1日単位)
                    'backupCount':7, #保存しておくログファイル数
                        },
                        },
# フォーマッタの設定
    'formatters': {
        'prod':{
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
            }


