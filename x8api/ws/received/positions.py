"""Module for X8 option websocket."""

def positions(api, message):
    if message["name"] == "positions":
        api.positions = message
