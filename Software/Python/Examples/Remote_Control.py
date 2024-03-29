#!/usr/bin/env python
#
# https://www.dexterindustries.com/GoPiGo/
# https://github.com/DexterInd/GoPiGo3
#
# Copyright (c) 2017 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information see https://github.com/DexterInd/GoPiGo3/blob/master/LICENSE.md
#
# This program uses the IR Receiver connected to AD1 with the Go Box IR remote to drive the GoPiGo3.

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import time    # import the time library for the sleep function
import gopigo3 # import the GoPiGo3 drivers

GPG = gopigo3.GoPiGo3() # Create an instance of the GoPiGo3 class. GPG will be the GoPiGo3 object.

try:
    GPG.set_grove_type(GPG.GROVE_1, GPG.GROVE_TYPE.IR_GO_BOX)
    value_last = -1
    while True:
        try:
            value = GPG.get_grove_value(GPG.GROVE_1)
            if value != value_last:
                value_last = value
                if value == 1:
                    GPG.set_motor_dps(GPG.MOTOR_LEFT ,  300)
                    GPG.set_motor_dps(GPG.MOTOR_RIGHT,  300)
                elif value == 2:
                    GPG.set_motor_dps(GPG.MOTOR_LEFT , -150)
                    GPG.set_motor_dps(GPG.MOTOR_RIGHT,  150)
                elif value == 4:
                    GPG.set_motor_dps(GPG.MOTOR_LEFT ,  150)
                    GPG.set_motor_dps(GPG.MOTOR_RIGHT, -150)
                elif value == 5:
                    GPG.set_motor_dps(GPG.MOTOR_LEFT , -300)
                    GPG.set_motor_dps(GPG.MOTOR_RIGHT, -300)
                else:
                    GPG.set_motor_dps(GPG.MOTOR_LEFT , 0)
                    GPG.set_motor_dps(GPG.MOTOR_RIGHT, 0)
        except IOError or gopigo3.SensorError:
            pass
    
except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    GPG.reset_all()       # Unconfigure the sensors, disable the motors, and restore the LED to the control of the GoPiGo3 firmware.
