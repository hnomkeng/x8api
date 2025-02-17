"""Module for base X8 option base websocket chanel."""
import time

class Base(object):
    """Class for base X8 option websocket chanel."""
    # pylint: disable=too-few-public-methods

    def __init__(self, api):
        """
        :param api: The instance of :class:`x8api
            <x8api.api.x8api>`.
        """
        self.api = api

    def send_websocket_request(self, name, msg,request_id=""):
        """Send request to X8 option server websocket.

        :param str name: The websocket chanel name.
        :param dict msg: The websocket chanel msg.

        :returns: The instance of :class:`requests.Response`.
        """
        if request_id == '':
            request_id = int(str(time.time()).split('.')[1])
        return self.api.send_websocket_request(name, msg,request_id)
