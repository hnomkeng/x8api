"""Module for X8 option websocket."""

def result(api, message):
    if message["name"] == "result":
        api.result = message["msg"]["success"]