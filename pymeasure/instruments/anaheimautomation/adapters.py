#
# This file is part of the PyMeasure package.
#
# Copyright (c) 2013-2021 PyMeasure Developers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#


from serial import rs485 as RS485
from pymeasure.adapters import SerialAdapter


class AnaheimMotorControllerSerialAdapter(SerialAdapter):
    """ Provides a :class:'SerialAdapter' with the specific baudrate,
    timeout, parity, and byte size for Anaheim Automation stepper motor controller
    serial communication.

    Initiates the adapter to open serial communication over the supplied
    port.


    :param port: A string representing the serial port. 
    :param idn: integer representing the identification number assigned to an individual motor
                controller. Values between 0-99 are valid.
    :param rs485: boolean to indicate if the rs485 communication protocol should be used. 
    """
    

    def __init__(self, port, idn):
        
        self.idn = idn

        super(AnaheimMotorControllerSerialAdapter, self).__init__(
            port,
            baudrate=38400,
            xonxoff=True,
            timeout=0.2,
            write_timeout=0.5
        )
       
    def write(self, command):
        """ Overwrites the :func:'SerialAdapter.write <pymeasure.adapters.SerialAdapter.write>'
        method to automatically prepend the motor controller id and append a carriage return to the command string.

        :param command: Command string to be sent to the instrument.
        """
        super(AnaheimMotorControllerSerialAdapter, self).write("@{}".format(self.idn) + command + "\r")



