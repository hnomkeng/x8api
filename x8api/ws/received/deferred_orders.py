"""Module for X8 option websocket."""

def deferred_orders(api, message):
    if message["name"] == "deferred-orders":
        api.deferred_orders = message