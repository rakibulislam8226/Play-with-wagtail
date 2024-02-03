from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&@e%k*o4&wz-$y6q!pca#kavhffm(04^)aqm8rv%7xh!(kri+o"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


ENABLE_SILK = os.environ.get("ENABLE_SILK", False) == "True"

if ENABLE_SILK:
    INSTALLED_APPS = [
        "silk",
    ] + INSTALLED_APPS
    MIDDLEWARE = [
        "silk.middleware.SilkyMiddleware",
    ] + MIDDLEWARE

try:
    from .local import *
except ImportError:
    pass
