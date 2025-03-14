"""Module for X8 option http loginv2 resource."""

from x8api.http.login import Login


class Loginv2(Login):
    """Class for X8 option loginv2 resource."""
    # pylint: disable=too-few-public-methods

    url = "/".join((Login.url, "v2"))

    def __init__(self, api):
        super(Loginv2, self).__init__(api)
