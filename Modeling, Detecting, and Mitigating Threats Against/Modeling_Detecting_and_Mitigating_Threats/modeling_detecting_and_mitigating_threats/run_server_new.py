#!/usr/bin/env python
"""Run Django development server with proper path setup."""
import os
import sys
import django
from pathlib import Path

# Get the directory containing this script
script_dir = Path(__file__).parent.absolute()

# Add to sys.path
sys.path.insert(0, str(script_dir))
os.chdir(str(script_dir))

# Set environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modeling_detecting_and_mitigating_threats.settings')
os.environ['PYTHONPATH'] = str(script_dir)

print(f"Working Directory: {os.getcwd()}")
print(f"PYTHONPATH: {os.environ['PYTHONPATH']}")
print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
print(f"sys.path[0]: {sys.path[0]}")

# Setup Django
try:
    django.setup()
    print("✓ Django setup successful")
except Exception as e:
    print(f"✗ Django setup failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Run Django development server
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line(['manage.py', 'runserver'])
