"""Module for X8 option websocket."""

def leaderboard_deals_client(api, message):
    if message["name"] == "leaderboard-deals-client":
        api.leaderboard_deals_client = message["msg"]