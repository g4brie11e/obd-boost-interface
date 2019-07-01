import obd, keyboard
from obd import OBDStatus


#--INSTALL NOTES
# Install python-OBD    https://python-obd.readthedocs.io/
# pip3 install obd
# Install keyboard detection module
# pip3 install keyboard

#linux: python (2.7)
#Macos: python3

# Install Android terminal emulator + keyboard helper

global retry
global connection

"""
Connect to the OBDII adapter through Bluetooth / usb??
"""
def connectOBDII():
    global connection
    connection = obd.OBD() # auto connect
    global retry

    # # OR
    # connection = obd.OBD("/dev/ttyUSB0") # create connection with USB 0
    # # OR
    # ports = obd.scan_serial()      # return list of valid USB or RF ports
    # print ports                    # ['/dev/ttyUSB0', '/dev/ttyUSB1']
    # connection = obd.OBD(ports[0]) # connect to the first port in the list

    #--TODO Test Bluetooth; only usb expected to work

    # Check if the connection was successful ('Not Connected', 'ELM Connected', 'OBD Connected' or 'Car Connected')
    if connection.status() == OBDStatus.CAR_CONNECTED:
        print('Successful connection to ' + connection.port_name())
    elif retry < 2: # Connection unsuccessful
        retry += 1
        print('Connection failed, restarting ...')
        connectOBDII()
    else:
        print('Connection not available, 3 attempts failed')

"""
Initialize OBDII adapter with AT commands;
"""
# def initOBDII():


"""
Continuously get data from the vehicle by issuing the corresponding PID codes.
"""
def process():
    global connection
    getData = False

    # Check that a valid connection has been made before allowing data flow
    if connection.status() != OBDStatus.CAR_CONNECTED:
        print('Check OBDII adapter and try again')
    else:
        getData = True

    while getData:
        # Do stuff with data
        x = connection.query(obd.commands.INTAKE_PRESSURE)
        # x /= 6.895 # Convert KPA to PSI

        print('boostPSI: ', x.value)

        # TODO:
        # Exit ??? How to do without keyboard in Android terminal?
        # if keyboard.is_pressed('q'): # exit key invoked
        #     print('Closing connection')
        #     connection.close()
        #     getData = False
        #     break


"""
Main entry point
"""
def main():
    global retry
    retry = 0

    connectOBDII()
    # initOBDII()
    process()



if __name__ == '__main__':
    main()
