"""Module for X8 option appinit http resource."""

from x8api.http.resource import Resource


class Appinit(Resource):
    """Class for X8 option login resource."""
    # pylint: disable=too-few-public-methods

    url = "appinit"

    def _get(self, data=None, headers=None):
        """Send get request for X8 option API appinit http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_http_request("GET", data=data, headers=headers)

    def __call__(self):
        """Method to get X8 option API appinit http request.

        :returns: The instance of :class:`requests.Response`.
        """
        return self._get()
