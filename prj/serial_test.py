import serial

ser = serial.Serial('COM3', 9600)
ser.flush()



while True:
    if ser.in_waiting > 0:

        data = ser.readline()  # Read data from the serial port
        #ser.flush()
        string = str(data, encoding='utf-8')

        print(data.decode('utf-8').strip())  # Decode and print the received data as a string
        #print(type(data.decode('utf-8').strip()))
        strs = data.decode('utf-8').strip()
        if strs.find('#') != -1:
            print(strs[10])
return 1

