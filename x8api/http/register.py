"""Module for X8 option register resource."""

from x8api.http.resource import Resource


class Register(Resource):
    """Class for X8 option register resource."""
    # pylint: disable=too-few-public-methods

    url = "register"
