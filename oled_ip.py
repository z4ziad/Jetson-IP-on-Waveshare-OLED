import serial
import json
import time
import socket

def get_ip_address():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            print(f"Got IP address: {ip}")
            return ip
        except Exception as e:
            print(f"Failed to get IP address: {e}, retrying...")
            time.sleep(1)

def open_serial():
    while True:
        try:
            ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
            print(f"Opened serial port: {ser.name}")
            return ser
        except Exception as e:
            print(f"Failed to open serial port: {e}, retrying...")
            time.sleep(1)

def display_ip():
    # [1] Keep trying until we get a valid IP
    ip = get_ip_address()

    # [2] Keep trying to open the serial port
    ser = open_serial()

    try:
        # [3] Display the IP address on line 1
        json_string = json.dumps({"T": 3, "lineNum": 1, "Text": "IP = " + ip}) + '\n'
        print(json_string.encode("utf-8"))
        ser.write(json_string.encode("utf-8"))
        ser.flush()
        time.sleep(1)

    except Exception as e:
        print(f"Error during communication: {e}")

    finally:
        # [4] Close the serial connection and exit
        if ser.is_open:
            ser.close()
            print("Serial port closed.")

    print("Done.")

display_ip()