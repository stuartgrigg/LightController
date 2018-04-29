from .plug_interface import PiMote


class LiveController(object):

    def __init__(self):
        self.on = False
        self.remote = PiMote()
        # Send a meesage to connect to the socket and ensure it is off.
        self.remote.send_message(1, False)

    def get_on(self):
        self._print_status()
        return self.on

    def set_on(self, on):
        self.remote.send_message(1, on)
        self.on = on
        self._print_status()
        return self.on

    def _print_status(self):
        print('Light is {}'.format('on' if self.on else 'off'))
