import os
import sdcard
import machine
import time

spi = machine.SPI(1, baudrate=1000000, polarity=0, phase=0, 
                  sck=machine.Pin(10), mosi=machine.Pin(11), miso=machine.Pin(12))
cs = machine.Pin(13, machine.Pin.OUT)

try:
    cs.high()
    time.sleep(1)
    sd = sdcard.SDCard(spi, cs)
    vfs = os.VfsFat(sd)
    os.mount(vfs, "/sd")
    print("SD card initialized successfully.")
except Exception as e:
    print("Failed to initialize SD card:", e)
    while True:
        pass

def list_files(directory="/sd", indent=0):
    try:
        for file in os.listdir(directory):
            path = f"{directory}/{file}"
            print("  " * indent + file, end="")
            try:
                if os.stat(path)[0] & 0x4000:  # Check if it's a directory
                    print("/")
                    list_files(path, indent + 1)
                else:
                    print(f" (size: {os.stat(path)[6]} bytes)")
            except OSError:
                print(" (error reading file)")
    except OSError as e:
        print("Error accessing directory:", e)

print("Files on SD card:")
list_files()

def read_file(filename="/sd/wokwi.txt"):
    try:
        with open(filename, "r") as f:
            print(f"\nContents of {filename}:")
            print(f.read())
    except OSError:
        print(f"Error opening {filename}!")

read_file()

while True:
    pass
