THIRD_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "django_extensions",
    "corsheaders",
    "cities_light",
    "django_rq",
    "admin_auto_filters",
]


PROJECT_APPS = [
    "users.apps.UsersConfig",
]
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
INSTALLED_APPS = THIRD_PARTY_APPS + PROJECT_APPS + DJANGO_APPS
