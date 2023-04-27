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
auth_token = ""

ZABBIX_API_URL = "https://zabbix.kolonet.uk/api_jsonrpc.php"


# USERNAME = "Admin"
# PASSWORD = "zabbix"

# # Login user
# # print("\nLogin user")
# def user_loging(ZABBIX_API_URL,USERNAME,PASSWORD):
#     req = requests.post(ZABBIX_API_URL,
#                     json = {
#                         "jsonrpc": "2.0",
#                         "method": "user.login",
#                         "params": {
#                                 "username": USERNAME,
#                                 "password": PASSWORD
#                         }, "id": 2,
#                     }, verify=False)
#     return req

# # print(json.dumps(req.json(), sort_keys=True, indent=4))

# user_loging = user_loging(ZABBIX_API_URL,USERNAME,PASSWORD)

# AUTHTOKEN = user_loging.json()["result"]


# Retrieve a list of problems
