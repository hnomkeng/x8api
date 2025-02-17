"""Module for X8 option http login resource."""

from x8api.http.resource import Resource


class Events(Resource):
    """Class for X8 option login resource."""
    # pylint: disable=too-few-public-methods

    url = ""

    def send_http(self,method, data=None, headers=None):
        """Send get request for X8 option API login http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.api.send_http_request_v2(method=method, url="https://event.8xtrade.com/api/v1/events",data=data)

    def __call__(self,method,data,headers=None):
        """Method to get X8 option API login http request.

        :param str username: The username of a X8 option server.
        :param str password: The password of a X8 option server.

        :returns: The instance of :class:`requests.Response`.
        """
         
         
        return self.send_http(method=method,data=data,headers=headers)
