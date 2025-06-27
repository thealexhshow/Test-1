#!/usr/bin/env python3
import os
from datetime import datetime

def timestamped_rename(folder='.'):
    for name in os.listdir(folder):
        if name.lower().endswith('.txt'):
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            new_name = f"{now}_{name}"
            os.rename(os.path.join(folder, name), os.path.join(folder, new_name))
            print(f"Renamed {name} → {new_name}")

if __name__ == '__main__':
    timestamped_rename()
