"""Module for X8 option http verify resource."""

from x8api.http.resource import Resource
import json


class Verify(Resource):
    """Class for X8 option verify resource."""
    # pylint: disable=too-few-public-methods

    url = ""

    def _post(self, data=None, headers=None):
        """Send get request for X8 option API verify http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.api.send_http_request_v2(method="POST", url="https://auth.8xtrade.com/api/v2/verify/2fa",data=json.dumps(data), headers=headers)

    def __call__(self, sms_received, token_sms):
        """Method to get X8 option API verify http request.

        :param str sms_received: The sms received of a X8 option server 2FA.
        :param str token_sms: The token of a X8 option server 2FA.

        :returns: The instance of :class:`requests.Response`.
        """
        data = {"code": str(sms_received),
                "token": token_sms}

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Referer': 'https://8xtrade.com/en/login',
            'Sec-Fetch-Mode': 'cors',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
            }

        return self._post(data=data, headers=headers)
