"""Module for X8 option http login resource."""

from x8api.http.resource import Resource


class Login2FA(Resource):
    """Class for X8 option login resource."""
    # pylint: disable=too-few-public-methods

    url = ""

    def _post(self, data=None, headers=None):
        """Send get request for X8 option API login http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.api.send_http_request_v2(method="POST", url="https://auth.8xtrade.com/api/v2/login",data=data, headers=headers)

    def __call__(self, username, password, token_login):
        """Method to get X8 option API login http request.

        :param str username: The username of a X8 option server.
        :param str password: The password of a X8 option server.
        :param str token: The token of a X8 option server 2FA.

        :returns: The instance of :class:`requests.Response`.
        """
        data = {"identifier": username,
                "password": password,
                "token": token_login}

        return self._post(data=data)
