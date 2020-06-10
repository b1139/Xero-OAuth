"""
Description: Manages the Oauth connection and related proceses
"""

import os
import json
from util import send_get_request, send_post_request
from config import *

# Set insecure security layer for dev
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


class Connection:
    """
    Class Manages the connection object Xero API
    Gets connection
    Refresh token
    """

    def __init__(self):
        # Token Retrieved
        self.token = None
        # Authorization code retrieved
        self.code = None
        # Tenant ID
        self.tenant_id = None
        # Refresh Token
        self.refresh_token = None
        # Creates connection and gets token
        self.get_connection()

    def get_connection(self):
        # Checks for existing refresh token
        if self.refresh_token:
            return 0
        login_url = Connection.get_auth_code()
        print(login_url)
        res = send_post_request(url=login_url, data=json.dumps({'Username': 'sathishkumarb1139@gmail.com',
                                                                'Password': 'saso2807'}))
        print("Click on the above link to get the Access code")
        self.code = ""  # code from the redirect URI
        # For now I read from user
        self.code = input("Enter Access Code: ")
        self.get_or_refresh_token()  # Now we have the token and refresh token
        self.get_tenant_id()  # This is to get the tenant Id in order to access API
        return self.token

    @staticmethod
    def get_auth_code():
        """
        Send a user to authorize your app
        :return: Response Object
        """
        params = {'response_type': 'code',
                  'client_id': CLIENT_ID,
                  'redirect_uri': REDIRECT_URI,
                  'scope': SCOPE,
                  'state': STATE}
        res = send_get_request(url=AUTHOURIZE_URI, params=params)
        return res.url

    def get_or_refresh_token(self):
        """
        Gets or Refresh token
        :return: token
        """
        headers = {'authorization': "Basic %s" % b64_client_id_secret,
                   'Content-Type': 'application/x-www-form-urlencoded'}
        data = {}
        if not self.token:
            data['grant_type'] = "authorization_code"
            data['code'] = self.code
            data['redirect_uri'] = REDIRECT_URI
        else:
            data['grant_type'] = "refresh_token"
            data['refresh_token'] = self.refresh_token

        res = send_post_request(url=TOKEN_URI, headers=headers, data=data)
        json_result = json.loads(res.text)
        self.token = json_result['access_token']
        self.refresh_token = json_result['refresh_token']

    def get_tenant_id(self):
        """
        Get tenent_id inorder to Consume APIs
        :return:
        """
        res = send_get_request(url=TENANT_URI, headers={'Authorization': "Bearer %s" % self.token,
                                                        'Content-Type': 'application/json'})
        json_ten = json.loads(res.text)[0]
        self.tenant_id = json_ten['tenantId']
