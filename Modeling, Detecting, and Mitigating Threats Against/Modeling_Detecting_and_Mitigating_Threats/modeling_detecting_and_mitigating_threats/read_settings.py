#!/usr/bin/env python
"""Simple settings reader."""
import os

settings_path = r'C:\Modeling, Detecting, and Mitigating Threats Against -20221213T140840Z-001\Modeling, Detecting, and Mitigating Threats Against\Modeling_Detecting_and_Mitigating_Threats\modeling_detecting_and_mitigating_threats\modeling_detecting_and_mitigating_threats\settings.py'

print(f"Checking: {settings_path}")
print(f"File exists: {os.path.exists(settings_path)}")

if os.path.exists(settings_path):
    with open(settings_path, 'r') as f:
        lines = f.readlines()
    
    print("\n=== SEARCHING FOR DATABASE CONFIGURATION ===\n")
    in_databases_section = False
    for i, line in enumerate(lines, 1):
        if 'DATABASES' in line and '=' in line:
            in_databases_section = True
            print(f"Line {i}: {line.rstrip()}")
        elif in_databases_section:
            print(f"Line {i}: {line.rstrip()}")
            if line.strip().startswith('}') and not line.rstrip().endswith(','):
                break
        
        # Also check for SECRET_KEY and DEBUG
        if 'SECRET_KEY' in line or 'DEBUG' in line or 'ALLOWED_HOSTS' in line:
            if not line.strip().startswith('#'):
                print(f"Line {i}: {line.rstrip()}")
