"""Module for X8 option websocket."""

def option_opened(api, message):
    if message["name"] == "option-opened":
        api.order_async[int(message["msg"]["option_id"])][message["name"]] = message