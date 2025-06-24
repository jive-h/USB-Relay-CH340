import keyboard
import subprocess
import sys

hotkey = 'ctrl+2'


def get_script():
    global script
    f = open('script_do', 'r')
    script = f.read()
    f.close()
    print("Script loaded successfully.")


def on_hotkey():
    p = subprocess.Popen(script, stdout=sys.stdout)
    p.communicate()
    if p.returncode != 0:
        print("Failed to execute the script.")
    else:
        print("Script executed.")

get_script()
while True:
    if keyboard.is_pressed(hotkey):
        while keyboard.is_pressed(hotkey):
            pass
        print("You pressed 2!")

        on_hotkey()
