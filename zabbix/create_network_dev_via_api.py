#!/usr/bin/python

# Create Devices in Zabbix Server via APIs:

import requests
import json
import urllib3
from datetime import datetime
from datetime import date

urllib3.disable_warnings()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
description = f"Host was added via ANSIBLE on {today} at {current_time}"

host_name = "vois2"
ip_addr = "10.81.0.235"
platform = "cisco_ios"


ZABBIX_API_URL = "https://zabbix.kolonet.uk/api_jsonrpc.php"
USERNAME = "Admin"
PASSWORD = "zabbix"

# Login user
# print("\nLogin user")
req = requests.post(ZABBIX_API_URL,
                json = {
                    "jsonrpc": "2.0",
                    "method": "user.login",
                    "params": {
                            "username": USERNAME,
                            "password": PASSWORD
                    }, "id": 2,
                }, verify=False)

# print(json.dumps(req.json(), sort_keys=True, indent=4))

AUTHTOKEN = req.json()["result"]

data ={
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": host_name,
        "interfaces": [
            {
                "type": 2,
                "main": 1,
                "useip": 1,
                "ip": ip_addr,
                "dns": "",
                "port": "161",
                "details": {
                "version": "2",
                "bulk": "1",
                "community": "{$SNMP_COMMUNITY}"
                }
            }
        ],
        "groups": [
            {
                "groupid": "22"
            }
        ],
        "tags": [
            {
                "tag": "platform",
                "value": platform
            },
                        {
                "tag": "api",
                "value": "ansible"
            },
        ],
        "templates": [
            {
                "templateid": "10218"
            }
        ],
        "inventory_mode": 1,
        "description": f"Host was added via ANSIBLE on {today}"
        #
        # "macros": [
        #     {
        #         "macro": "{$USER_ID}",
        #         "value": "123321"
        #     },
            #   {
            #      "description": "Added via ansible"
            #   }
        #     {
        #         "macro": "{$USER_LOCATION}",
        #         "value": "0:0:0",
        #         "description": "latitude, longitude and altitude coordinates"
        #     }
        # ],
    },
    "id": 2,
    "auth": AUTHTOKEN
}

# Retrieve a list of problems

req = requests.post(ZABBIX_API_URL, json = data , verify=False)
# print(json.dumps(req.json(), sort_keys=True, indent=4))

result = req.json()["result"]
if result != "":
    print(f"\nHost {host_name} was added successfully! ")
    print (result)
else:
    # create entry in error.log
    pass

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