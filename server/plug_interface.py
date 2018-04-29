# import the required modules
import time

import RPi.GPIO as GPIO


class PiMote(object):
    def __init__(self):
        self.gpio_setup()

    def gpio_setup(self):
        GPIO.cleanup()
        # set the pins numbering mode
        GPIO.setmode(GPIO.BOARD)
        # Select the GPIO pins used for the encoder K0-K3 data inputs
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        # Select the signal used to select ASK/FSK
        GPIO.setup(18, GPIO.OUT)
        # Select the signal used to enable/disable the modulator
        GPIO.setup(22, GPIO.OUT)
        # Disable the modulator by setting CE pin lo
        GPIO.output(22, False)
        # Set the modulator to ASK for On Off Keying
        # by setting MODSEL pin lo
        GPIO.output(18, False)
        # Initialise K0-K3 inputs of the encoder to 0000
        GPIO.output(11, False)
        GPIO.output(15, False)
        GPIO.output(16, False)
        GPIO.output(13, False)

    def get_code(self, socket, is_on):
        if socket < 0 or socket > 4:
            raise ValueError('Invalid socket')
        out = 0
        if is_on:
            out += 8
        if socket == 0:
            out += 3
        else:
            out += 4
            out += (4 - socket)
        return out

    def send_message(self, socket, is_on):
        if socket < 1 or socket > 4:
            raise ValueError('Invalid socket')
        # socket zero corresponds to all sockets
        code = self.get_code(socket, is_on)
        GPIO.output(13, code // 8)
        GPIO.output(16, code // 4)
        GPIO.output(15, code // 2)
        GPIO.output(11, code // 1)
        # let it settle, encoder requires this
        time.sleep(0.1)
        # Enable the modulator
        GPIO.output(22, True)
        # keep enabled for a period
        time.sleep(0.25)
        # Disable the modulator
        GPIO.output(22, False)

    def gpio_cleanup(self):
        GPIO.cleanup()
