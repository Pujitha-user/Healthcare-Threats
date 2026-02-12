# 🚀 FREE DEPLOYMENT GUIDE - Django Project

## Overview of Free Hosting Options

### ⭐ Best Options (Recommended)

1. **PythonAnywhere** - Easiest for Django, MySQL included
2. **Render** - Modern, free SSL, PostgreSQL included
3. **Railway** - Good for beginners, free tier
4. **Fly.io** - Great performance, free tier

---

## 🎯 OPTION 1: PythonAnywhere (EASIEST - RECOMMENDED)

### Pros:
- ✅ Free tier specifically for Python/Django
- ✅ MySQL database included
- ✅ Easy to configure
- ✅ No credit card required
- ✅ Direct file upload

### Free Tier Limits:
- 1 web app
- 512 MB storage
- MySQL database included
- Always-on web app

### Step-by-Step Deployment:

#### 1. Create Account
- Go to: https://www.pythonanywhere.com/
- Sign up for a FREE "Beginner" account
- Verify your email

#### 2. Upload Your Project
- Click "Files" tab
- Create directory: `/home/yourusername/myproject`
- Upload all files from: `C:\Modeling\Modeling, Detecting, and Mitigating Threats Against\Modeling_Detecting_and_Mitigating_Threats\modeling_detecting_and_mitigating_threats\`
- OR use Git to clone (recommended)

#### 3. Setup Virtual Environment
Open a Bash console:
```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
pip install django==3.2.25
pip install mysqlclient
pip install pandas numpy scikit-learn
pip install xlwt
```

#### 4. Setup MySQL Database
- Go to "Databases" tab
- Note your database details:
  - Host: `yourusername.mysql.pythonanywhere-services.com`
  - Database name: `yourusername$modeling_db`
  - Username: `yourusername`
  - Password: (set your own)

#### 5. Update settings.py
```python
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourusername$modeling_db',
        'USER': 'yourusername',
        'PASSWORD': 'your_password',
        'HOST': 'yourusername.mysql.pythonanywhere-services.com',
    }
}

DEBUG = False  # Important for production!

STATIC_ROOT = '/home/yourusername/myproject/static'
STATIC_URL = '/static/'
```

#### 6. Import Database
- Go to "Databases" tab
- Click on "Mysql console" for your database
- Run your SQL file or migrate:
```bash
cd /home/yourusername/myproject
python manage.py migrate
```

#### 7. Setup Web App
- Go to "Web" tab
- Click "Add a new web app"
- Choose "Manual configuration" → Python 3.10
- Set source code: `/home/yourusername/myproject`
- Set working directory: `/home/yourusername/myproject`
- Edit WSGI file to point to your project

#### 8. Configure WSGI File
Click on WSGI configuration file and replace with:
```python
import os
import sys

path = '/home/yourusername/myproject'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'modeling_detecting_and_mitigating_threats.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### 9. Collect Static Files
In Bash console:
```bash
cd /home/yourusername/myproject
python manage.py collectstatic
```

#### 10. Reload Web App
- Go to "Web" tab
- Click "Reload" button
- Visit: `https://yourusername.pythonanywhere.com`

---

## 🎯 OPTION 2: Render (Modern, Free SSL)

### Pros:
- ✅ Free PostgreSQL database
- ✅ Automatic HTTPS
- ✅ Git-based deployment
- ✅ Modern interface

### Free Tier Limits:
- Web service sleeps after 15 mins of inactivity
- 750 hours/month
- PostgreSQL database (90 days retention)

### Step-by-Step Deployment:

#### 1. Prepare Project Files

Create `requirements.txt`:
```txt
Django==3.2.25
mysqlclient==2.2.7
pandas==2.3.3
numpy==2.2.6
scikit-learn==1.7.2
xlwt==1.3.0
gunicorn==21.2.0
psycopg2-binary==2.9.9
whitenoise==6.6.0
```

Create `build.sh`:
```bash
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

Create `render.yaml`:
```yaml
databases:
  - name: modelingdb
    databaseName: modeling_db
    user: modeling_user

services:
  - type: web
    name: modeling-threats
    runtime: python
    buildCommand: "./build.sh"
    startCommand: "gunicorn modeling_detecting_and_mitigating_threats.wsgi:application"
    envVars:
      - key: PYTHON_VERSION
        value: 3.10.0
      - key: DATABASE_URL
        fromDatabase:
          name: modelingdb
          property: connectionString
```

#### 2. Update settings.py for Render
Add to settings.py:
```python
import dj_database_url

ALLOWED_HOSTS = ['*']  # Update with your render domain

# For PostgreSQL on Render
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://localhost/modeling_db',
        conn_max_age=600
    )
}

# Static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

#### 3. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

#### 4. Deploy on Render
- Go to: https://render.com/
- Sign up for free
- Click "New +" → "Web Service"
- Connect your GitHub repository
- Render will auto-detect and deploy
- Visit your app URL

---

## 🎯 OPTION 3: Railway (Easiest Git Deployment)

### Pros:
- ✅ Very easy setup
- ✅ Free tier ($5 credit/month)
- ✅ PostgreSQL included
- ✅ No credit card for trial

### Step-by-Step:

#### 1. Prepare Files
Same as Render (requirements.txt, etc.)

Create `Procfile`:
```
web: gunicorn modeling_detecting_and_mitigating_threats.wsgi --log-file -
```

Create `railway.json`:
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python manage.py migrate && python manage.py collectstatic --no-input && gunicorn modeling_detecting_and_mitigating_threats.wsgi",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

#### 2. Deploy
- Go to: https://railway.app/
- Sign up with GitHub
- Click "New Project" → "Deploy from GitHub repo"
- Select your repository
- Add PostgreSQL database from Railway
- Set environment variables
- Deploy automatically

---

## 📝 Production Checklist

Before deploying, update these in settings.py:

```python
# Security Settings
DEBUG = False
SECRET_KEY = 'your-new-secret-key-generate-one'  # Generate new one!
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']

# Database - Use environment variables
import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '3306',
    }
}

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

---

## 🆓 Free Tier Comparison

| Platform | Database | Uptime | Ease | Best For |
|----------|----------|--------|------|----------|
| PythonAnywhere | MySQL ✅ | Always-on | ⭐⭐⭐⭐⭐ | Your project (MySQL) |
| Render | PostgreSQL | Sleeps | ⭐⭐⭐⭐ | Modern apps |
| Railway | PostgreSQL | Limited hours | ⭐⭐⭐⭐ | Quick deploy |
| Fly.io | PostgreSQL | 3 VMs free | ⭐⭐⭐ | Performance |

---

## 🎯 RECOMMENDED FOR YOUR PROJECT:

**Use PythonAnywhere** because:
1. ✅ You're already using MySQL (no migration needed)
2. ✅ Easiest Django deployment
3. ✅ Free MySQL database included
4. ✅ Always-on (no sleep)
5. ✅ No credit card required
6. ✅ Perfect for your tech stack

---

## 📞 Need Help?

Common Issues:
- **Static files not loading**: Run `collectstatic`
- **Database errors**: Check credentials and migrations
- **Import errors**: Install all requirements in virtual env
- **500 errors**: Check error logs and set DEBUG=True temporarily

Your app will be live at:
- PythonAnywhere: `https://yourusername.pythonanywhere.com`
- Render: `https://yourapp.onrender.com`
- Railway: `https://yourapp.up.railway.app`
