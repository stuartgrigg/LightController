class TestController(object):

    def __init__(self):
        self.on = False

    def get_on(self):
        self._print_status()
        return self.on

    def set_on(self, on):
        self.on = on
        self._print_status()
        return self.on

    def _print_status(self):
        print('Light is {}'.format('on' if self.on else 'off'))
