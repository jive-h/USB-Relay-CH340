import keyboard
import subprocess
import sys
import serial
import serial.tools.list_ports as port_list
import time
    
hotkey = 'ctrl+shift+2'
cmdOn = [0xA0, 0x01, 0x01, 0xA2]
cmdOff = [0xA0, 0x01, 0x00, 0xA1]

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


def on_hoykey_PySerial():
    # Configure the serial port
    # Replace 'COMx' with your actual serial port (e.g., 'COM3' on Windows, '/dev/ttyUSB0' on Linux)
    # Set the baud rate to match your device
    try:
        ser = serial.Serial(
            port='COM3',        # Change this to your serial port
            baudrate=9600,      # Change this to your device's baud rate
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=1           # Timeout in seconds for read operations
        )
    except serial.SerialException as ex:
        print(f"Error opening serial port: {ex}")
        exit()

    if ser.isOpen():
        print(f"Serial port {ser.name} opened successfully.")
        try:
            # Write data to the serial port
            ser.write(cmdOn)
            #print(f"Sent: {cmdOn.decode().strip()}")
            print("Sent: On")

            time.sleep(0.05) # Give some time for the device to respond

            ser.write(cmdOff)
            #print(f"Sent: {cmdOff.decode().strip()}")
            print("Sent: Off")
            

        except Exception as e:
            print(f"Communication error: {e}")
        finally:
            ser.close()
            print("Serial port closed.")
    else:
        print("Failed to open serial port.")

def show_COM_list():
    ports = list(port_list.comports())
    for p in ports:
        print (p)

def free_cpu():
    time.sleep(0.001)
    
get_script()
show_COM_list()
while True:
    if keyboard.is_pressed(hotkey):
        #on_hotkey()
        on_hoykey_PySerial()
        print("You pressed 2!")

        while keyboard.is_pressed(hotkey):
            free_cpu()
            pass

    free_cpu()
