# StartupMacro
This script is utilized for the game Bee Swarm Simulator on roblox and works with any resolution. You must be using Windows OS and have python installed.

# Requirements:
Python 3.0 or higher: https://www.youtube.com/watch?v=yivyNCtVVDk (tutorial on how to install python) 
A vip server
Natro macro installed: https://github.com/NatroTeam/NatroMacro

# First, edit the file
To be able to run this startup macro, you need to make sure that your vip server link and natro are put into the python script.
1. First, Download the code by clicking the green "code" ---> download zip button, and Extract the folder called StartupMacro-main.zip when it is finished.
2. Go to the python file, right click it, and open it with notepad.

DO NOT CHANGE anything else, just put your vip server where it says to do so, and put the link to the path of your natro macro folder.

3. Then press Ctrl + s and close out of notepad. 

You are done with this step!



# To run and test:
First, you need to test that the python script works and functions properly. 


Click the windows key and type in command prompt. Then, change your directory to the working one in command prompt.
Paste this command in
```
cd Downloads\StartupMacro-main\StartupMacro-main\ShySkill Startup Macro V1.0
```
Third, download the required packages
paste this in:
```
pip install -r requirements.txt
```
then run the file and test it by pasting this into command prompt
```
python ShySkill-Macro-V1.0.py
```

## How to set up auto launch on startup

1. Click the windows home button and type in task scheduler.
2. Once in task scheduler, go to the "Task Scheduler Library" folder on the left hand side.
3. Click "Create Task"
4. Give the task a name and desc (optional), and check the box that says "Run whether user is logged on or not"
5. Create a new trigger and under begin the task put 'At Startup"
6. Then go to Actions and put in the following:
7. Action: Start a program
8.  In the program/script box, put the path to your installation of python. You can check this by clicking the windows button, typing python, and then clicking open file location and clicking copy path. (add the image of the documentation.)
9.  In the arguments section, put the path of the startup macro python file. Example: "C:\Users\ShySkill\Downloads\StartupMacro-main\StartupMacro-main\ShySkill Startup Macro V1.0\ShySkill-Macro-V1.0.py"
10.  For the start in section, just leave it blank. Then you can press Ok and then Ok.

Then you should be set up! Message me on discord or open an issue if there are any problems. 

