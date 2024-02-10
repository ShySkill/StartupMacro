import time, keyboard, webbrowser, pyautogui, subprocess, os, requests

#starts up roblox and claims the hive
# starts up roblox and claims the hive

import os

def fetchLink():

    username = os.getlogin()
    path = os.path.join(r"C:\Users", username, "Downloads\\StartupMacro-main\\StartupMacro-main\\ShySkill Startup Macro V1.0\\linktoserver.txt")
    file_path = path

    try:
        file = open(file_path, "r", encoding='utf-8')
        content = file.read()
    
        print("File contents (visible):\n" + content)

        return content
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)
    finally:
        if 'file' in locals():
            file.close()







def startUpRoblox():
    # opens roblox and waits for it to load (30 seconds for 2.50ghz+, 60 seconds for )
    # put your vip server link. It should look like: webbrowser.open_new('https://www.roblox.com/share?code=203f00aa3&type=Server')
    webbrowser.open_new(fetchLink())
    honey_location = None
    max_attempts = 8
    attempts = 0
    natro_location = None

    username = os.getlogin()
    path = os.path.join(r"C:\Users", username, "Downloads\\StartupMacro-main\\StartupMacro-main\\ShySkill Startup Macro V1.0\\pollenimage.PNG")
    
    while attempts < max_attempts and honey_location is None:
        time.sleep(10)
        try:
            honey_location = pyautogui.locateOnScreen(path)
        except pyautogui.ImageNotFoundException:
            print("Image not found. Retrying...")
            attempts += 1

    if honey_location is None:
        print(f"Image not found after {max_attempts} attempts. Exiting.")
        return

    # Roblox has finished loading, and you are now waiting at spawn

    # Closes the browser to minimize CPU usage
    keyboard.press("alt+tab")
    time.sleep(0.2)
    keyboard.release("alt+tab")
    time.sleep(0.8)
    keyboard.press("alt+F4")
    time.sleep(0.2)
    keyboard.release("alt+F4")
    # Runs to the center hive and claims it
    time.sleep(10)
    pressHoldKey("w", 2)
    for i in range(0, 10):
        keyboard.press_and_release("e")
        time.sleep(1)
        keyboard.press_and_release("e")  
#C:\Users\ShySkill\Downloads\Natro Macro
def makeFirstFolderPath():
    winUsername = os.getlogin()
    str1 = "C:\\Users\\"
    str2 = "\\Downloads\\Natro Macro\\"
    folderPath = str1 + winUsername + str2

    return folderPath


def getRecentVersion():
    response = requests.get("https://api.github.com/repos/NatroTeam/NatroMacro/releases/latest")
    version = response.json()["name"]
    version = version[13:20]
    return version


current_version = getRecentVersion()

def get_folders_in_directory(directory_path):
    folders = [f for f in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, f))]
    return folders

def get_user_version():
    folders = get_folders_in_directory(makeFirstFolderPath())
    #01234567891123456718
    #Natro Macro v0.9.8
    folders = [element[13:20] for element in folders]
    user_version = max(folders)
    return user_version

#get the version of the user and add that to the first folder path, then return the path for startupnatro
def get_final_path():
    str1 = makeFirstFolderPath()
    str2 = "Natro Macro v"
    str3 = str(get_user_version())

    final_path = str1 + str2 + str3
    return final_path
    #Natro Macro v0.9.9.1
    #first string + (Natro Macro v) + second string 

def startUpNatro():
    try:
        #natro path is the users path
        natro_path = get_final_path()
        os.system(f'cmd /c "cd {natro_path} && START.bat"')
        user_ver = get_user_version()
        #updated path is the most recent from github
        print(user_ver + ": is user current version")
        print(current_version + ": is natro current version")
        if(user_ver != current_version):
            print("updating")
            updateNatro()

        return True

    except subprocess.CalledProcessError as e:
        print(f"Error Running the Natro Macro. Check provided file path. Shutting down and trying again.")
        return False

#(press tab 7 times then enter)
def updateNatro():
    for i in range(0, 9):
        keyboard.press_and_release("TAB")
        time.sleep(0.7)
    keyboard.press_and_release("ENTER")
    time.sleep(40)
    print(str(get_user_version()) + " is the new user version!")
    if(get_user_version() == current_version):
        print("update successful!")

#main press and hold
def pressHoldKey(key_to_hold, hold_duration):

    start_time = time.time()
    while time.time() - start_time < hold_duration:
        phk(key_to_hold, 0.1)  

    keyboard.release(key_to_hold)

#@param key and duration are passed here
#press and hold the key
def phk(key, duration):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

#change this if needed
#coundown is normally 10 seconds but can be changed.
countdown = 10

def loadWindowsAndWait():
    print("Python File Executed. Launching VIP server link to Bee Swarm Simulator in " + str(countdown) + " seconds. ")
    print("StartupMacro is succesfully running.")
    
    for i in range(0, countdown):
        time.sleep(1)
        print("Countdown: " + str(i))

def startMacro():
    time.sleep(10)
    for i in range(0, 3):
        keyboard.press("F1")
        keyboard.release("F1")
        time.sleep(0.5)


def main():
    #Wait for windows to load
    loadWindowsAndWait()
    #start up roblox and claim the hive
    startUpRoblox()
    #start up natro and update if necessary
    startUpNatro()
    #start the macro by pressing f1 after natro is loaded
    startMacro()

if __name__ == "__main__":
    main()
    quit()

