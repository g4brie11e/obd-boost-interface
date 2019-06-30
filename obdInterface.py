# First install python-OBD
# https://python-obd.readthedocs.io/

import obd

""" 
Connect to the OBDII adapter through Bluetooth / usb?? 
"""
def connectOBDII():
    connection = obd.OBD() # auto connect

    # # OR
    # connection = obd.OBD("/dev/ttyUSB0") # create connection with USB 0
    # # OR
    # ports = obd.scan_serial()      # return list of valid USB or RF ports
    # print ports                    # ['/dev/ttyUSB0', '/dev/ttyUSB1']
    # connection = obd.OBD(ports[0]) # connect to the first port in the list

    #--TODO Test bluetooth; only usb expected to work

    # Check if the connection was successful ('Not Connected', 'ELM Connected', 'OBD Connected' or 'Car Connected')
    if connection.status() == OBDStatus.CAR_CONNECTED:
        print('Successful connection to ' + connection.port_name())
    else: # Connection unsuccessful
        print('Connection failed, restarting ...')
        connectOBDII()




""" 
Initialize OBDII adapter with AT commands; 
"""
def initOBDII():


""" 
Continuously get data from the vehicle by issuing the corresponding PID codes.
"""
def process():
    getData, exitNow = True
    while getData:
        # Do stuff with data
        x = connection.query(obd.commands.MONITOR_BOOST_PRESSURE_B1)

        #--TODO convert monitor object to printable text
        # https://python-obd.readthedocs.io/en/latest/Responses/#monitors-mode-06-responses

        print('boostPSI: ' + x) 

        # Exit ??? How to do without keyboard in Android terminal?
        if exitNow: # exit invoked
            connection.close()
            getData = False


""" Main entry point """
def main():
    connectOBDII()
    # initOBDII()
    process()



