"""
Description: Manages the invoices
             Support CRUD Operation of invoices
             Xero API
"""

import json
from connection import Connection
from util import send_get_request, parse_xml, send_put_request, send_post_request
from config import INVOICE_API_URL, INVOICE_CREATE


class Invoices:
    """
    Creates a data pipeline for the Xero Invoices
    """

    def __init__(self):
        # This is a connection object which is ready to consume the API
        self.conn = Connection()

    def get(self):
        """
        Retrieves invoices
        :return: List of invoices
        """
        # Refresh token
        self.conn.get_or_refresh_token()
        headers = {'authorization': "Bearer %s" % self.conn.token,
                   'Content-Type': 'application/json',
                   'Xero-tenant-id': self.conn.tenant_id}
        res = send_get_request(url=INVOICE_API_URL, headers=headers)
        # Parses the XML to Python Dictionary
        invoices = parse_xml(res.text)
        invoices = invoices['Response']['Invoices']['Invoice']

        return invoices

    def post(self):
        """
        Updates invoices
        :return:
        """
        pass

    def put(self):
        """
        Creates Invoices
        :return:
        """
        # Refresh token
        self.conn.get_or_refresh_token()
        headers = {'authorization': "Bearer %s" % self.conn.token,
                   'Content-Type': 'application/json',
                   'Xero-tenant-id': self.conn.tenant_id}

        res = send_put_request(url=INVOICE_API_URL, headers=headers, data=json.dumps(INVOICE_CREATE))
        # print(res.text)
        invoices = parse_xml(res.text)
        invoices = invoices['Response']['Invoices']['Invoice']
        return invoices


# inv = Invoices()
# invoices_list = inv.get()


# print("Fetching Invoices...")
# print(f"Invoice Count: {len(invoices_list)}")
# print(invoices_list)

# print("Creating Invoices")
# invoices_list = inv.put()
# print(invoices_list)

# invoices_list = inv.get()
# print(f"Invoice Count: {len(invoices_list)}")

from config import *

def get_or_refresh_token():
    """
    Gets or Refresh token
    :return: token
    """
    # headers = {'authorization': "Basic %s" % b64_client_id_secret,
    #            'Content-Type': 'application/x-www-form-urlencoded'}
    data = {}

    data['grant_type'] = "client_credentials"
    data['client_id'] = CLIENT_ID
    data['client_secret'] = CLIENT_SECRET

    res = send_post_request(url=TOKEN_URI, headers=None, data=json.dumps(data))
    json_result = json.loads(res.text)
    print(json_result)
get_or_refresh_token()