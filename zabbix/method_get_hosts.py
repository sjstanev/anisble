#!/usr/bin/python

# Create Devices in Zabbix Server via APIs:

import requests
import json
import urllib3
...
urllib3.disable_warnings()

def get_host_via_api():

    ZABBIX_API_URL = "https://zabbix.kolonet.uk/api_jsonrpc.php"
    USERNAME = "Admin"
    PASSWORD = "zabbix"

    req = requests.post(ZABBIX_API_URL,
                    json = {
                        "jsonrpc": "2.0",
                        "method": "user.login",
                        "params": {
                                "username": USERNAME,
                                "password": PASSWORD
                        }, "id": 2,
                    }, verify=False)

    AUTHTOKEN = req.json()["result"]

    data ={
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": [
                    "hostid",
                    "host"
                ],
                "selectInterfaces": [
                    "interfaceid",
                    "ip"
                ]
            },
            "id": 2,
            "auth": AUTHTOKEN
        }

    req = requests.post(ZABBIX_API_URL, json = data , verify=False)

    result = req.json()["result"]

    req = requests.post(ZABBIX_API_URL,
                    json={
                        "jsonrpc": "2.0",
                        "method": "user.logout",
                        "params": {},
                        "id": 2,
                        "auth": AUTHTOKEN
                    }, verify=False)

    return result

get_host_via_api()