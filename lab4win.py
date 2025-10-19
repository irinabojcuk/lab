import os
import shutil

os.makedirs('AA/AA1', exist_ok=True)
os.makedirs('AA/AA2/11', exist_ok=True)
os.makedirs('BB', exist_ok=True)

windows_path = r'C:\Windows'
target_path_aa = 'AA'
target_path_bb = 'BB'

for filename in os.listdir(windows_path):
    src_file = os.path.join(windows_path, filename)
    if filename.startswith('S') and os.path.isfile(src_file):
        shutil.copy2(src_file, os.path.join(target_path_aa, filename))
        shutil.copy2(src_file, os.path.join(target_path_bb, f'new_{filename}'))

devices = [
    "Monitor",
    "Keyboard",
    "Mouse",
    "CPU",
    "RAM",
    "HardDrive"
]

devices_file = os.path.join('AA', 'AA1', 'devices.txt')
with open(devices_file, 'w') as f:
    for device in devices:
        f.write(device + '\n')

shutil.copy2(devices_file, os.path.join('AA', 'AA2', '11', 'hardware.SSS'))

print("\n=== Tree structure ===")
for root, dirs, files in os.walk('.', topdown=True):
    level = root.replace('.', '').count(os.sep)
    indent = ' ' * 4 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 4 * (level + 1)
    for f in files:
        print(f"{subindent}{f}")

print("\n=== Contents of hardware.SSS ===")
hardware_file = os.path.join('AA', 'AA2', '11', 'hardware.SSS')
with open(hardware_file, 'r') as f:
    print(f.read())

#shutil.rmtree('AA')
#shutil.rmtree('BB')
#print("All created files and directories have been deleted.")
 
