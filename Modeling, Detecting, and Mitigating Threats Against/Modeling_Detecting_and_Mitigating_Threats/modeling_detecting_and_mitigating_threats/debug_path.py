import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_path)

print(f"Current path: {current_path}")
print(f"Sys path: {sys.path}")
print(f"Dir contents: {os.listdir(current_path)}")

try:
    import modeling_detecting_and_mitigating_threats
    print(f"Imported package: {modeling_detecting_and_mitigating_threats}")
    print(f"Package file: {modeling_detecting_and_mitigating_threats.__file__}")
except ImportError as e:
    print(f"Import failed: {e}")

try:
    from modeling_detecting_and_mitigating_threats import settings
    print("Imported settings successfully")
except ImportError as e:
    print(f"Settings import failed: {e}")
