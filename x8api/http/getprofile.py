"""Module for X8 option http getprofile resource."""

from x8api.http.resource import Resource


class Getprofile(Resource):
    """Class for X8 option getprofile resource."""
    # pylint: disable=too-few-public-methods

    url = "getprofile"

    def _get(self):
        """Send get request for X8 option API getprofile http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_http_request("GET")

    def __call__(self):
        """Method to get X8 option API getprofile http request.

        :returns: The instance of :class:`requests.Response`.
        """
        return self._get()
