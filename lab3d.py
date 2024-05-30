#!/usr/bin/env python3
# Author ID: rlamoste

import os
import subprocess

def free_space():
    free_spaceoutput = subprocess.getoutput("df -h | grep '/$' | awk '{print $4}'")
    return free_spaceoutput.strip()

if __name__ == "__main__":
    print(free_space())
