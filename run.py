#!/usr/bin/env python

# import keyboard
import sys
import obd
from obd import OBDStatus

# NOTE: current 'failed to choose baud' issue on MacOS (sees the OBD-II adapter's port but fails)
#       ideas to try: turn ignition on, try on not MacOS

# TODO: interactive cmd line gui
# TODO: install Android terminal emulator + keyboard helper
# TODO: test with bluetooth
# TODO: run on RPI

class OBDII_interface:
    def __init__(self):
        """
        Initialise the OBDII adapter connection through RF or USB
        """
        print("\t>> Attempting to connect to OBD ...")
        self.connection = obd.OBD() # auto-connect
        # self.connection = obd.OBD( protocol="8", baudrate=9600, fast=False, timeout=30) 
        self.status = self.connection.status()

    def initOBDII(self):
        """
        Initialize OBDII adapter with AT commands;
        """
        # TODO
        pass

    def process(self):
        """
        Continuously get data from the vehicle by issuing the corresponding PID codes.
        """
        a = self.connection.query(obd.commands.ELM_VOLTAGE)
        print(f"OBD-II adapter voltage: {a.value}")

        # Boost output
        x = self.connection.query(obd.commands.INTAKE_PRESSURE)
        x /= 6.895 # convert KPA to PSI
        print(f"boostPSI: {x.value}")
        
        y = self.connection.query(obd.commands.GET_DTC)
        print(f"DTCs: {y.value}")

        x = self.connection.query(obd.commands.OIL_TEMP)
        print(f"Engine oil temp: {x.value}•C")

        # TODO: Exit upon Android volume key press?

        # TODO: Exit 'q' press
        # if keyboard.is_pressed('q'): # exit key invoked
        #     print('Closing connection')
        #     connection.close()
        #     getData = False
        #     break

if __name__ == '__main__':
    obd.logger.setLevel(obd.logging.DEBUG)
    test = OBDII_interface()

    # Check if the connection was successful ('Not Connected', 'ELM Connected', 'OBD Connected' or 'Car Connected')
    if test.status != OBDStatus.CAR_CONNECTED:
        print("\t >> Connection not available, exiting ...")
        sys.exit()

    test.process()
