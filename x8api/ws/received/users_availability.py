"""Module for X8 option websocket."""

def users_availability(api, message):
    if message["name"] == "users-availability":
        api.users_availability = message["msg"]