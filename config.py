"""
Description: Holds the configurable master variables for the system
"""
import base64

CLIENT_ID = '8C1A58B40831416C922641980616EC73'
CLIENT_SECRET = 'lZJuAbBR6VCRq-g5DhCFag2vlosZuy4d_vsMuMWsMH4qpUND'
REDIRECT_URI = "https://www.google.co.in"

AUTHOURIZE_URI = 'https://login.xero.com/identity/connect/authorize'
TOKEN_URI = "https://identity.xero.com/connect/token"
TENANT_URI = "https://api.xero.com/connections"
INVOICE_API_URL = "https://api.xero.com/api.xro/2.0/Invoices"
SCOPE = "openid profile email accounting.transactions"
STATE = "123"
b64_client_id_secret = base64.b64encode((CLIENT_ID + ":" + CLIENT_SECRET).encode()).decode()


# Added the Required fields
# This will create a invoice
INVOICE_CREATE = {
  "Type": "ACCREC", # Mandatory
  "Contact": {
    # This is a static ID I have taken from the API Viewer
    "ContactID": "96a480f3-a034-4bfc-a12d-48715acaae09" # mandatory
  },
  "DateString": "2020-04-02T19:00:00",
  "DueDateString": "2020-04-10T16:00:00",
  "LineAmountTypes": "Exclusive",
  "LineItems": [
    {
      "Description": "Red Sweater for Testing",
      "Quantity": "500",
      "ItemCode": "8090" # Mandatory (Copied from Xero web application
    }
  ]
}