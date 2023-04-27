#!/usr/bin/python

# USER LogOut

import requests
import json
import urllib3


urllib3.disable_warnings()


ZABBIX_API_URL = "https://zabbix.kolonet.uk/api_jsonrpc.php"


urllib3.disable_warnings()

# Logout user
# print("\nLogout user")
req = requests.post(ZABBIX_API_URL,
                  json={
                      "jsonrpc": "2.0",
                      "method": "user.logout",
                      "params": {},
                      "id": 2,
                      "auth": AUTHTOKEN
                  }, verify=False)

print(json.dumps(req.json(), sort_keys=True, indent=4))