"""Module for X8 option websocket."""

def financial_information(api, message):
    if message["name"] == "financial-information":
            api.financial_information = message