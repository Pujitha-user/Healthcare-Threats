import sys
import os

# Add the current directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modeling_detecting_and_mitigating_threats.settings')

# Run Django development server
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'runserver'])
