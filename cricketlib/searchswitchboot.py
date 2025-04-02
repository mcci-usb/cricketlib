import serial
import serial.tools.list_ports
import time

TARGET_VID_PID = "VID:PID=045E:0646"  # Target USB device VID:PID
STATUS_CMD = "status\r\n"

def check_status(myport):
    """Check the device model after sending a status command."""
    try:
        ser = serial.Serial(
            myport, baudrate=115200, bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE, timeout=1, stopbits=serial.STOPBITS_ONE
        )
        time.sleep(0.5)  # Reduce sleep time to allow faster scanning

        ser.write(STATUS_CMD.encode())  # Send the status command
        response = ser.readlines()  # Read all available lines

        ser.close()  # Ensure port is closed

        # Check if response contains "Model 3141"
        for line in response:
            decoded_line = line.decode('utf-8').strip()
            if "Model 3141" in decoded_line:
                return "3141"  # Detected Model 3141
            elif "Model 3142" in decoded_line:
                return "3142"
            
        return None  # No valid response found
    except serial.SerialException as e:
        print(f"Error opening {myport}: {e}")
        return None  # Handle cases where the port cannot be opened
    except Exception as e:
        print(f"Unexpected error on {myport}: {e}")
        return None  # Handle any other unexpected errors


def find_switch():
    """Search for connected COM ports and detect all Model 3141 devices."""
    comlist = serial.tools.list_ports.comports()
    detected_ports = []

    # print("\n--- Scanning available COM ports ---")
    for port, desc, hwid in sorted(comlist):
        # print(f"Checking: {port}, {desc}, {hwid}")
        
        if TARGET_VID_PID in hwid:  # Check if VID:PID matches
            # print(f"Found target device at {port}")
            model = check_status(port)
            if model == "3141":
                result = f"{model}({port})"  # Format as "3141(COMx)"
                # print(f"Detected {result}")
                detected_ports.append(result)
            elif model == "3142":
                result = f"{model}({port})"  # Format as "3141(COMx)"
                # print(f"Detected {result}")
                detected_ports.append(result)
            else:
                print(f"No valid response from {port}")
                detected_ports.append(port)  # Append only COMx if not 3141
        # else:
        #     detected_ports.append(port)  # Append non-target devices as COMx

    # if detected_ports:
    #     for dp in detected_ports:
    #         print(dp)  # Print formatted detected ports

    return detected_ports if detected_ports else None
