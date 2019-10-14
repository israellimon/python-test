import os
from datetime import timedelta

CLIENT_SECRET = "LV+UYz:P*3mn3/FM1yqw7x41gJochQ.9" # Our Quickstart uses this placeholder
# In your production app, we recommend you to use other ways to store your secret,
# such as KeyVault, or environment variable as described in Flask's documentation here
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

#AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
AUTHORITY = "https://login.microsoftonline.com/60cd6759-54c7-4620-98ec-865dd3bc66d6"
# AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

CLIENT_ID = "8ee27ff0-7a50-4744-b5ba-61163d765b27"

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All"]

SESSION_COOKIE_NAME = 'puto'
m = timedelta(minutes=5)
PERMANENT_SESSION_LIFETIME = m
SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session
SESSION_PERMANENT = True
