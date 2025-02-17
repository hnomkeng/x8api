"""Module for X8 option websocket."""

def order_canceled(api, message):
    if message["name"] == "order-canceled":
        api.order_canceled = message