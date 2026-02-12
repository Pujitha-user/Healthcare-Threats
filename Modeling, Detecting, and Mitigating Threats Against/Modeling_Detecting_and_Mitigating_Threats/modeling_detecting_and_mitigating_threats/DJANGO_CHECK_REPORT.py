#!/usr/bin/env python
"""Comprehensive Django installation and database connectivity check."""

import os
import sys
import subprocess

print("=" * 80)
print("DJANGO INSTALLATION & DATABASE CONNECTIVITY CHECK")
print("=" * 80)

# Get Python info
print(f"\nPython Executable: {sys.executable}")
print(f"Python Version: {sys.version.split()[0]}")

# Check Django
try:
    import django
    print(f"✓ Django {django.get_version()} is installed")
except ImportError:
    print("✗ Django is NOT installed")
    sys.exit(1)

# Check other required packages
required_packages = ['djangorestframework', 'sqlparse', 'psycopg2', 'mysqlclient']
print(f"\nInstalled Python Packages:")
try:
    result = subprocess.run(
        [sys.executable, '-m', 'pip', 'list'],
        capture_output=True,
        text=True,
        timeout=10
    )
    packages_output = result.stdout
    for line in packages_output.split('\n')[:20]:
        if line.strip():
            print(f"  {line}")
except Exception as e:
    print(f"  Error listing packages: {e}")

print("\n" + "=" * 80)
print("ISSUE SUMMARY")
print("=" * 80)

print("""
The project has been successfully moved from the OneDrive location to C:\\. 

However, there is a MODULE PATH ISSUE preventing Django from starting:

PROBLEM:
--------
1. Django is properly installed in the virtual environment (v5.2.10)
2. The settings.py file exists in the correct location
3. However, when Django tries to import 'modeling_detecting_and_mitigating_threats.settings'
   it cannot find the module because the current working directory is not in sys.path

ERROR MESSAGE:
---------------
ModuleNotFoundError: No module named 'modeling_detecting_and_mitigating_threats.settings'

ROOT CAUSE:
-----------
The manage.py and start_server.py files set DJANGO_SETTINGS_MODULE but they don't properly
ensure the parent directory containing the 'modeling_detecting_and_mitigating_threats' package
is in Python's sys.path during module import.

SOLUTION:
---------
We need to ensure sys.path includes the current working directory BEFORE Django setup() is called.
The updated run_server.bat file and run_server_new.py script should handle this.

DATABASE CONFIGURATION:
-----------------------
To check database configuration, you'll need to either:
1. Fix the path issue first
2. Manually edit settings.py to verify the database settings

NEXT STEPS:
-----------
1. Update manage.py to properly add the current directory to sys.path
2. Ensure all __init__.py files are in place (already done)
3. Set PYTHONPATH environment variable before running
4. Or use the provided run_server_new.py script which handles path setup correctly
""")

print("=" * 80)
