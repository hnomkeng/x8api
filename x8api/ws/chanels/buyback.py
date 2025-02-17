"""Module for X8 option buyback websocket chanel."""

from x8api.ws.chanels.base import Base


class Buyback(Base):
    """Class for X8 option subscribe to buyback websocket chanel."""
    # pylint: disable=too-few-public-methods

    name = "buyback"

    def __call__(self):
        """Method to send message to buyback websocket chanel."""
        pass
