from .base import *
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'ProjectInfo',
        'Trusted_Connection':'yes',
        'HOST':'DESKTOP-VBORAD3\SQLEXPRESS',
        'OPTIONS':{
            'driver':'SQL Server Native Client 11.0'
        },
    },
}
