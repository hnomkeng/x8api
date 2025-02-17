"""Module for X8 option http auth resource."""

from x8api.http.resource import Resource


class Auth(Resource):
    """Class for X8 option http auth resource."""
    # pylint: disable=too-few-public-methods

    url = "auth"
