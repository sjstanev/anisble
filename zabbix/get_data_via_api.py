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

# data ={
#         "jsonrpc": "2.0",
#         "method": "host.get",
#         "params": {
#             "output": [
#                 "hostid",
#                 "host"
#             ],
#             "selectInterfaces": [
#                 "interfaceid",
#                 "ip"
#             ]
#         },
#         "id": 2,
#         "auth": AUTHTOKEN
#     }


# data = {
#      "jsonrpc": "2.0",
#      "method": "template.get",
#      "params": {
#          "output": "extend",
#          "filter": {
#              "host": [
#                  "Linux by Zabbix agent",
#                  "Cisco IOS by SNMP",
#                   "Mikrotik by SNMP"
#              ]
#          }
#      },
#      "id": 2,
#      "auth": AUTHTOKEN
# }


data = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
        "filter": {
            "name": [
                "Cisco Switches",
                "Mikrotik"
            ]
        }
    },
    "id": 2,
    "auth": AUTHTOKEN
}



# data = {
#     "jsonrpc": "2.0",
#     "method": "map.get",
#     "params": {
#         "output": "extend",
#         "selectSelements": "extend",
#         "selectLinks": "extend",
#         "selectUsers": "extend",
#         "selectUserGroups": "extend",
#         "selectShapes": "extend",
#         "selectLines": "extend",
#         #"sysmapids": "3"
#     },
#     "id": 2,
#     "auth": AUTHTOKEN
# }
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