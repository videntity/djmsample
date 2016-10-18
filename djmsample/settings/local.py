from .base import *

#ROOT_URLCONF = 'djmsample.urls_local'

# INSTALLED_APPS = (
# 
# 
# 
# 
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
# 
#     # Djmongo Apps
#     'djmongo',
#     'djmongo.console',
#     'djmongo.search',
# 
#     # 'apps.djmongo.dataimport',
#     'djmongo.accounts',
#     'djmongo.write',
#     'djmongo.aggregations',
# 
# 
#     # 3rd party
#     'corsheaders',
#     'bootstrapform',
#     'widget_tweaks',
# 
# )

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10
}
