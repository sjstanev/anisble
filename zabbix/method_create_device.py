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

host_name = "vois22"
ip_addr = "10.81.0.235"
platform = "cisco_ios"


ZABBIX_API_URL = "https://zabbix.kolonet.uk/api_jsonrpc.php"
USERNAME = "Admin"
PASSWORD = "zabbix"

# LogIn user
# print("\nLogin user")
def user_login(ZABBIX_API_URL,USERNAME,PASSWORD):
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

# Create device
def create_device(auth_token, hostname = host_name, ip_addr = ip_addr, platform = platform):
    templateid = '10218'
    groupid = '22'

    if platform == 'Cisco':
        templateid = '10218'
        groupid = '22'

    elif platform == 'MikroTik':
        templateid = '10233'
        groupid = '23'


    data ={
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": hostname,
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
                    "groupid": groupid
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
                    "templateid": templateid
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
        "auth": auth_token
    }

    req = requests.post(ZABBIX_API_URL, json = data , verify=False)
    # print(json.dumps(req.json(), sort_keys=True, indent=4))

    result = req.json()["result"]
    if result != "":
        print(f"\nHost {hostname} was added successfully! ")
        #print (result)
    else:
        # create entry in error.log
        pass


# LogOut user
# print("\nLogout user")
def user_logout(auth_token):
    req = requests.post(ZABBIX_API_URL,
                    json={
                        "jsonrpc": "2.0",
                        "method": "user.logout",
                        "params": {},
                        "id": 2,
                        "auth": auth_token
                    }, verify=False)
    # print('Loged Out')
    # print(json.dumps(req.json(), sort_keys=True, indent=4))


# if __name__ == "__main__":

# Create first device in zabbix
def create_single_devic_via_ansible(hostname = host_name, ip_addr = ip_addr, platform = platform):

    user_login_success = user_login(ZABBIX_API_URL,USERNAME,PASSWORD)
    # Create TOKEN
    auth_token = user_login_success.json()["result"]

    # Create Device
    create_device(auth_token, hostname, ip_addr, platform)

    # LogOut
    user_logout(auth_token)


# Create other devices in zabbix
def create_multiple_devic_via_ansible(hostname, ip_addr, platform):


    user_login_success = user_login(ZABBIX_API_URL,USERNAME,PASSWORD)
    # Create TOKEN
    auth_token = user_login_success.json()["result"]

    # Create Device
    create_device(auth_token, hostname, ip_addr, platform)

    # LogOut
    user_logout(auth_token)


