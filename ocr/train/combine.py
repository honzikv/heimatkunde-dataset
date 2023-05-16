import os
import shutil

prefix = 'heimatkunde-a15539_'
folders = [f for f in os.listdir() if f.startswith(prefix) and os.path.isdir(f)]
output_folder = 'combined'

os.makedirs(output_folder, exist_ok=True)

for folder in folders:
    files = os.listdir(folder)
    for file in files:
        shutil.copy(os.path.join(folder, file), os.path.join(output_folder, f'{folder}_{file}'))
