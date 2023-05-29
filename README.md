# KILLAPP
This repo contains a small python app which kills user specified process on Windows after startup.
My personal use for this is to kill any RGB software after setup. \
To add a new process to this project look for the .exe in taskmanager and add it to the process list inside the 
`KillApp.py` file

### Prerequisist
- Python
- Packages of requirements.txt

### Building
Optional but recommended to first build a venv in which the requirements.txt should be installed.\
To build the .exe run the following command in the project directory:

``` bash
pyinstaller --onefile --noconsole KillApp.py
```
The final .exe will be created and stored in /dist.
This can be added to you windows startup folder. 

### Current limitations
only user process can be killed no system processes.