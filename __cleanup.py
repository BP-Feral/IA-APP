# Created on Thu May 16 2024
# Copyright (c) 2024 BP Feral
# Python 3.12.1

# ===================================================================
import shutil, os
# ===================================================================

from colorama import Fore
# ===================================================================

def warn(message):
    print(Fore.YELLOW + f"[!] " + message  + Fore.RESET)

def clean_project():
    dir = '__pycache__'
    locations = ['./', './classes', './scenes']

    for location in locations:
        try:
            path = os.path.join(location, dir)
            shutil.rmtree(path)
        except:
            warn(f"There is no cache in {location}")

    try:
        shutil.rmtree('./build')
    except:
        warn(f"There were no builds to clear")

    try:
        shutil.rmtree('./dist')
    except:
        warn(f"There were no dists to clear")

    try:
        os.remove('./AI.spec')
    except:
        warn(f"There was no spec file to remove")

    print(Fore.GREEN + "Cleanup Complete!" + Fore.RESET)

# ===================================================================
clean_project()