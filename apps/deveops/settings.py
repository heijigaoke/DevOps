# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 09 13:49
# Author Yo
# Email YoLoveLife@outlook.com
"""
Django settings for devEops project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import django.db.backends.mysql

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1x$!#dwp2_6^tdgs1nv8pwgutbc#4m%#qaz!m!0h_f*%6fp+vt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'validate.apps.ValidateConfig',
    'softlib.apps.SoftlibConfig',
    'manager.apps.ManagerConfig',
    'operation.apps.OperationConfig',
    'application.apps.MagicConfig',
    'authority.apps.AuthorityConfig',
    'execute.apps.ExecuteConfig',
    'concert.apps.ConcertConfig',
    'timeline.apps.TimelineConfig',
    'rest_framework',
    'bootstrap3',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

REST_FRAMEWORK = {
    # 'PAGE_SIZE':10,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'deveops.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'deveops.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# if 'BUILD_ON_TRAVIS' in os.environ:
#     DATABASES={
#         'default':{
#             'ENGINE':'django.db.backends.mysql',
#             'NAME':'deveops_testdb',
#             'USER':'root',
#             'PASSWORD':'',
#             'HOST':'127.0.0.1',
#             'PORT':'3306',
#         },
#     }
# else:
DATABASES={
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'deveopsdb',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# I18N translation
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'), ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

LOGIN_URL='/validate/login'
AUTH_USER_MODEL='validate.ExtendUser'

SESSION_SAVE_EVERY_REQUEST=True
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SESSION_COOKIE_AGE=15*60

#LDAP
from django_auth_ldap.config import LDAPSearch,GroupOfNamesType
import ldap
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
AUTH_LDAP_SERVER_URI = "ldap://10.100.61.6:389"
AUTH_LDAP_BIND_DN = "cn=tools,ou=Zabbix,ou=TEST,dc=zbjt,dc=com"
AUTH_LDAP_BIND_PASSWORD = "7a$LIOOwxNO"

OU = unicode('ou=信息安全与运维中心,ou=集团所属公司,ou=浙报集团,dc=zbjt,dc=com','utf8')
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(OU,ldap.SCOPE_SUBTREE,"(objectClass=groupOfNames)")
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")
AUTH_LDAP_USER_SEARCH = LDAPSearch(OU,ldap.SCOPE_SUBTREE,"(&(objectClass=*)(sAMAccountName=%(user)s))")
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name":"givenName",
    "last_name":"sn",
    "email":"userPrincipalName",
    "phone":"mobile",
}
AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_MIRROR_GROUPS = True