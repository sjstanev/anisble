#!/usr/bin/python

# USER LogIn

import requests
import json
import urllib3


urllib3.disable_warnings()


ZABBIX_API_URL = "https://zabbix.kolonet.uk/api_jsonrpc.php"
USERNAME = "Admin"
PASSWORD = "zabbix"

# LogIn user
# print("\nLogin user")
def user_loging(ZABBIX_API_URL,USERNAME,PASSWORD):
    req = requests.post(ZABBIX_API_URL,
                    json = {
                        "jsonrpc": "2.0",
                        "method": "user.login",
                        "params": {
                                "username": USERNAME,
                                "password": PASSWORD
                        }, "id": 2,
                    }, verify=False)
    return req

# print(json.dumps(req.json(), sort_keys=True, indent=4))

user_loging = user_loging(ZABBIX_API_URL,USERNAME,PASSWORD)

AUTHTOKEN = user_loging.json()["result"]

print(AUTHTOKEN)

# LogOut user
# print("\nLogout user")
def user_logout(ZABBIX_API_URL):
    req = requests.post(ZABBIX_API_URL,
                    json={
                        "jsonrpc": "2.0",
                        "method": "user.logout",
                        "params": {},
                        "id": 2,
                        "auth": AUTHTOKEN
                    }, verify=False)
    print('Loged Out')
    #print(json.dumps(req.json(), sort_keys=True, indent=4))

user_logout = user_logout(ZABBIX_API_URL)

