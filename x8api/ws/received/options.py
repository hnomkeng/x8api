"""Module for X8 option websocket."""

def option(api, message):
    if message["name"] == "options":
        api.get_options_v2_data = message