"""Module for X8 option websocket."""

def position(api, message):
    if message["name"] == "position":
        api.position = message
