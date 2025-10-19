import os
import shutil
from pathlib import Path

os.makedirs('AA/AA1', exist_ok=True)
os.makedirs('AA/AA2/11', exist_ok=True)
os.makedirs('BB', exist_ok=True)

home_dir = Path.home()
target_path_aa = Path('AA')
target_path_bb = Path('BB')

for item in os.listdir(home_dir):
    src_file = home_dir / item
    if item.startswith('S') and src_file.is_file():
        shutil.copy2(src_file, target_path_aa / item)
        shutil.copy2(src_file, target_path_bb / f'new_{item}')

devices = [
    "Monitor",
    "Keyboard",
    "Mouse",
    "CPU",
    "RAM",
    "HardDrive"
]

devices_file = Path('AA/AA1/devices.txt')
with open(devices_file, 'w') as f:
    for device in devices:
        f.write(device + '\n')

shutil.copy2(devices_file, Path('AA/AA2/11/hardware.SSS'))

print("\n=== Tree structure ===")
for root, dirs, files in os.walk('.'):
    level = root.replace('.', '').count(os.sep)
    indent = ' ' * 4 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 4 * (level + 1)
    for file in files:
        print(f"{subindent}{file}")

print("\n=== Contents of hardware.SSS ===")
hardware_file = Path('AA/AA2/11/hardware.SSS')
with open(hardware_file, 'r') as f:
    print(f.read())

#shutil.rmtree('AA')
#shutil.rmtree('BB')
#print("All created files and directories have been deleted.")


