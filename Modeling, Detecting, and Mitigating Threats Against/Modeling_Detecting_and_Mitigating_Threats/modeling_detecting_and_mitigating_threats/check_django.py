#!/usr/bin/env python
"""Check Django installation and database connectivity."""
import os
import sys

# Add current directory to path FIRST
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
sys.path.insert(0, '.')

# Change to current directory to ensure proper imports
os.chdir(current_dir)

print("=" * 60)
print("DJANGO INSTALLATION & CONNECTION CHECK")
print("=" * 60)

# Check Python version
print(f"\nPython Version: {sys.version}")
print(f"Current Directory: {os.getcwd()}")
print(f"Script Location: {current_dir}")

# Check Django installation
try:
    import django
    print(f"\n✓ Django is installed: v{django.VERSION}")
except ImportError as e:
    print(f"\n✗ Django is NOT installed: {e}")
    sys.exit(1)

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modeling_detecting_and_mitigating_threats.settings')

# Try to setup Django
try:
    django.setup()
    print("✓ Django setup successful")
except Exception as e:
    print(f"✗ Django setup failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Check settings
try:
    from django.conf import settings
    print("\n" + "=" * 60)
    print("DATABASE CONFIGURATION")
    print("=" * 60)
    
    for db_alias, db_config in settings.DATABASES.items():
        print(f"\n[{db_alias}]")
        for key, value in db_config.items():
            if key == 'PASSWORD':
                print(f"  {key}: ****")
            else:
                print(f"  {key}: {value}")
    
    print("\n" + "=" * 60)
    print("CHECKING DATABASE CONNECTIONS")
    print("=" * 60)
    
    from django.db import connections
    from django.db.utils import OperationalError
    
    for db_alias in settings.DATABASES.keys():
        try:
            connection = connections[db_alias]
            connection.ensure_connection()
            print(f"\n✓ {db_alias} connection successful")
            
            # Try a simple query
            with connection.cursor() as cursor:
                if settings.DATABASES[db_alias]['ENGINE'] == 'django.db.backends.sqlite3':
                    cursor.execute("SELECT 1")
                elif 'mysql' in settings.DATABASES[db_alias]['ENGINE']:
                    cursor.execute("SELECT 1")
                elif 'postgresql' in settings.DATABASES[db_alias]['ENGINE']:
                    cursor.execute("SELECT 1")
                else:
                    cursor.execute("SELECT 1")
                result = cursor.fetchone()
                print(f"  Test query result: {result}")
        except OperationalError as e:
            print(f"\n✗ {db_alias} connection FAILED: {e}")
        except Exception as e:
            print(f"\n✗ {db_alias} error: {e}")
    
    print("\n" + "=" * 60)
    print("INSTALLED APPS")
    print("=" * 60)
    for app in settings.INSTALLED_APPS:
        print(f"  - {app}")
    
    print("\n" + "=" * 60)
    print("✓ All checks completed!")
    print("=" * 60)
    
except Exception as e:
    print(f"\n✗ Error checking settings: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
