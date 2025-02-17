"""Module for X8 option http login resource."""

from x8api.http.resource import Resource


class Logout(Resource):
    """Class for X8 option login resource."""
    # pylint: disable=too-few-public-methods

    url = ""

    def _post(self, data=None, headers=None):
        """Send get request for X8 option API login http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.api.send_http_request_v2(method="POST", url="https://auth.8xtrade.com/api/v1.0/logout",data=data, headers=headers)

    def __call__(self):
       
        return self._post()

