import time, keyboard, webbrowser, pyautogui, subprocess, os

#starts up roblox and claims the hive
def startUpRoblox():
    #opens roblox and waits for it to load (30 seconds for 2.50ghz+, 60 seconds for )
    #put your vip server link. It should look like: webbrowser.open_new('https://www.roblox.com/share?code=203f00aa3&type=Server')
    webbrowser.open_new('put your vip server in here') 
    time.sleep(40)

    #roblox has finished loading and you are now waiting at spawn

    #closes the browser to minimize CPU usage
    keyboard.press("alt+tab")
    time.sleep(0.2)
    keyboard.release("alt+tab")
    time.sleep(0.8)
    keyboard.press("alt+F4")
    time.sleep(0.2)
    keyboard.release("alt+F4")
    #runs to the center hive and claims it
    time.sleep(1)
    pressHoldKey("w", 2)
    keyboard.press("e")
    keyboard.release("e")
    keyboard.press("e")
    keyboard.release("e")


def startUpNatro():
    try:
        #an example of this would be C:\Users\User\Downloads\Natro_Macro_v0.9.8\Natro Macro v0.9.8
        natro_path = r'C:\Users\User\Downloads\Natro_Macro_v0.9.8\Natro Macro v0.9.8'
        os.system(f'cmd /c "cd {natro_path} && START.bat"')
        time.sleep(10)
        keyboard.press("F1")

    except subprocess.CalledProcessError as e:
        print(f"Error Running the Natro Macro. Shutting down and trying again.")

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

def loadWindowsAndWait():
    print("Python File Executed. Launching VIP server link to Bee Swarm Simulator")
    print("StartupMacro is succesfully running.")
    
    for i in range(0, 10):
        time.sleep(1)
        print("Countdown: " + str(i))

def main():
    loadWindowsAndWait()
    startUpRoblox()
    startUpNatro()

if __name__ == "__main__":
    main()
    quit()
