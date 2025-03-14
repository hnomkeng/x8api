"""Module for X8 option changebalance resource."""

from x8api.http.resource import Resource
from x8api.http.profile import Profile


class Changebalance(Resource):
    """Class for X8 option changebalance resource."""
    # pylint: disable=too-few-public-methods

    url = "/".join((Profile.url, "changebalance"))

    def _post(self, data=None, headers=None):
        """Send get request for X8 option API changebalance http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_http_request("POST", data=data, headers=headers)

    def __call__(self,balance_id):
        """Method to get X8 option API changebalance http request.

        :param str balance_id: The balance identifier.

        :returns: The instance of :class:`requests.Response`.
        """
        data = {"balance_id": balance_id}
        return self._post(data)
