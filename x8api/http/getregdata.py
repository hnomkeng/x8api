"""Module for X8 option http getregdata resource."""

from x8api.http.resource import Resource
from x8api.http.register import Register


class Getprofile(Resource):
    """Class for X8 option getregdata resource."""
    # pylint: disable=too-few-public-methods

    url = "/".join((Register.url, "getregdata"))

    def _get(self):
        """Send get request for X8 option API getregdata http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_http_request("GET")

    def __call__(self):
        """Method to get X8 option API getregdata http request.

        :returns: The instance of :class:`requests.Response`.
        """
        return self._get()
