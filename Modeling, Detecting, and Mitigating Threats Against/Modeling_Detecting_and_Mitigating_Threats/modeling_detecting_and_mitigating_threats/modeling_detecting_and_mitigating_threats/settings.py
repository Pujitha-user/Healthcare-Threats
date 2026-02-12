# Settings.py

# Django settings for the project

SECRET_KEY = 'YOUR_SECRET_KEY_HERE'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
        'USER': 'YOUR_DB_USER_HERE',
        'PASSWORD': 'YOUR_DB_PASSWORD_HERE',
    }
}