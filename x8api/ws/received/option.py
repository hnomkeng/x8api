"""Module for X8 option websocket."""

def option(api, message):
    if message["name"] == "option":
        api.buy_multi_option[str(message["request_id"])] = message["msg"]