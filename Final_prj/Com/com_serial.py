import serial
import time
#ser = serial.Serial('COM3', 9600)
def atp_seial(com, baudrate):
    ser = serial.Serial(com,baudrate)
    ser.flush()
    while True:
        if ser.in_waiting > 0:

            data = ser.readline()  # Read data from the serial port
            #ser.flush()
            string = str(data, encoding='utf-8')

            print(data.decode('utf-8').strip())  # Decode and print the received data as a string
            strs = data.decode('utf-8').strip()
            if strs.find('#') != -1:
                ser.close()
                return strs[10]

def pta_serial(com, baudrate): #pc to computer
    ser = serial.Serial(com, baudrate)
    ser.flush()
    i = 0
    while i < 20:
        string = '1\n'
        ser.write(bytes(string, 'utf-8'))
        time.sleep(0.05)
        i = i+1
        # if ser.in_waiting > 0:
        #     data = ser.readline()
        #     print(data.decode('utf-8').strip())

    ser.close()

def reset():
    ser = serial.Serial('COM3', 9600)
    time.sleep(1)
    ser.close()