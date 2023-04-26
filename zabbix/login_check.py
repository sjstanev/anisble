#!/usr/bin/python

# Create Devices in Zabbix Server via APIs:

import requests
import json
import urllib3
...
urllib3.disable_warnings()

ZABBIX_API_URL = "https://zabbix.kolonet.uk/api_jsonrpc.php"
USERNAME = "Admin"
PASSWORD = "zabbix"

#Login user
print("\nLogin user")
req = requests.post(ZABBIX_API_URL,
                json = {
                    "jsonrpc": "2.0",
                    "method": "user.login",
                    "params": {
                            "username": USERNAME,
                            "password": PASSWORD
                    }, "id": 1
                }, verify=False)

print(json.dumps(req.json(), sort_keys=True, indent=4))

AUTHTOKEN = req.json()["result"]

# Retrieve a list of problems
print("\nRetrieve a list of problems")
req = requests.post(ZABBIX_API_URL,
                  json={
                      "jsonrpc": "2.0",
                      "method": "problem.get",
                      "params": {
                          "output": "extend", 
                          "selectAcknowledges": "extend", 
                          "recent": "true", 
                          "sortfield": ["eventid"],
                          "sortorder": "DESC"
                      },
                      "id": 2,
                      "auth": AUTHTOKEN
                  }, verify=False)

print(json.dumps(req.json(), sort_keys=True, indent=4))

#Logout user
print("\nLogout user")
req = requests.post(ZABBIX_API_URL,
                  json={
                      "jsonrpc": "2.0",
                      "method": "user.logout",
                      "params": {},
                      "id": 2,
                      "auth": AUTHTOKEN
                  }, verify=False)

print(json.dumps(req.json(), sort_keys=True, indent=4))