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

##Login user
print("\nLogin user")
req = requests.post(ZABBIX_API_URL,
                json = {
                    "jsonrpc": "2.0",
                    "method": "user.login",
                    "params": {
                            "username": USERNAME,
                            "password": PASSWORD
                    }, "id": 2,
                }, verify=False)

print(json.dumps(req.json(), sort_keys=True, indent=4))

AUTHTOKEN = req.json()["result"]

data ={
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "Linux server2",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.3.1",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "4"
            }
        ],
        # "tags": [
        #     {
        #         "tag": "Host name",
        #         "value": "Linux server"
        #     }
        # ],
        "templates": [
            {
                "templateid": "10001"
            }
        ]
        # "macros": [
        #     {
        #         "macro": "{$USER_ID}",
        #         "value": "123321"
        #     },
        #     {
        #         "macro": "{$USER_LOCATION}",
        #         "value": "0:0:0",
        #         "description": "latitude, longitude and altitude coordinates"
        #     }
        # ],
        # "inventory_mode": 0,
        # "inventory": {
        #     "macaddress_a": "01234",
        #     "macaddress_b": "56768"
        # }
    },
    "id": 2,
    "auth": AUTHTOKEN
}

# Retrieve a list of problems
print("\nGet hosts")
req = requests.post(ZABBIX_API_URL, json = data , verify=False)

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