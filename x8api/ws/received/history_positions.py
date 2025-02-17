"""Module for X8 option websocket."""

def history_positions(api, message):
    if message["name"] == "history-positions":
        api.position_history_v2 = message