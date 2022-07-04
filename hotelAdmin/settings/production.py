from hotelAdmin.settings.settings import *
import dj_database_url

SECRET_KEY = 'django-insecure-dku(3*(n=-7=v&i-lyxedu7xn*_-9hiju^psw6476#07hj#4az'

DEBUG = False

# Alterar para o IP do ambiente de produção quando houver.
ALLOWED_HOSTS = ['hotelprojec.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}
