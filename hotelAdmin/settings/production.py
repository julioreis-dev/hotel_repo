from hotelAdmin.settings.settings import *
import dj_database_url

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

# Alterar para o IP do ambiente de produção quando houver.
ALLOWED_HOSTS = ['hotelproject-app.herokuapp.com']


DATABASES = {
    'default': dj_database_url.config()
}
