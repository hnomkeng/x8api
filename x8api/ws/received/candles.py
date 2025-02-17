"""Module for X8 option websocket."""

def candles(api, message):
    if message['name'] == 'candles':
        try:
            api.candles.candles_data = message["msg"]["candles"]
        except:
            pass