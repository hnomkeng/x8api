"""Module for X8 option websocket."""

def instruments(api, message):
    if message["name"] == "instruments":
            api.instruments = message["msg"]