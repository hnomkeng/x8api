"""Module for X8 option billing resource."""

from x8api.http.resource import Resource


class Billing(Resource):
    """Class for X8 option billing resource."""
    # pylint: disable=too-few-public-methods

    url = "billing"
