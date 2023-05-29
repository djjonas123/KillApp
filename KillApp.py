"""
Create an .exe with the below command:

pyinstaller --onefile --noconsole KillApp.py
"""

import time
import subprocess

if __name__ == '__main__':
    #Sleep to allow for setup of program before killing.
    time.sleep(15)

    #Call terminate can be replaced with delete
    CREATE_NO_WINDOW = 0x08000000

    #list with processes to be terminated
    processes = ['NZXT CAM.exe', 'cam_helper.exe', 'hid.exe']

    for p in processes:
        # os.system("wmic process where name='"+ p +"' call terminate")
        subprocess.call("wmic process where name='"+ p +"' call terminate", creationflags=CREATE_NO_WINDOW)

