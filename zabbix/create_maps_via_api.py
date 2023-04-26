#!/usr/bin/python

# Create Devices in Zabbix Server via APIs:

import requests
import json
import urllib3
from datetime import datetime


urllib3.disable_warnings()



ZABBIX_API_URL = "https://zabbix.kolonet.uk/api_jsonrpc.php"
USERNAME = "Admin"
PASSWORD = "zabbix"

# Login user
req = requests.post(ZABBIX_API_URL,
                json = {
                    "jsonrpc": "2.0",
                    "method": "user.login",
                    "params": {
                            "username": USERNAME,
                            "password": PASSWORD
                    }, "id": 1,
                }, verify=False)


AUTHTOKEN = req.json()["result"]

# get information about hostid, hostname and etc. using tag filter 
get_hosts_ids ={
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": [
                "hostid",
                "host",
                "groupids",
            ],
            "selectTags": "extend",
            "evaltype": 0,
            "tags": [
                {
                    "tag": "api",
                    "value": "ansible",
                    "operator": 1
                }
            ],
            "selectInterfaces": [
                "interfaceid",
                "ip"
            ]
        },
        "id": 2,
        "auth": AUTHTOKEN
    }

request_get_hosts_id = requests.post(ZABBIX_API_URL, json = get_hosts_ids , verify=False)
#print(json.dumps(request_get_hosts_id.json(), sort_keys=True, indent=4))

result = request_get_hosts_id.json()["result"]

host_via_api = False
value_is_ansible = False
device_list = []

# create list that containt dictionary with nessessory device information to create maps
def create_device(result):

    for _ in range(int(len(result))):
        result = request_get_hosts_id.json()["result"][_]
        for i in range(len(result["tags"])):

            # check whether this device is added via api and has tag ansible
            if result["tags"][i]["tag"] == 'api':
                host_via_api = True
            if  result["tags"][i]["value"] == 'ansible':
                value_is_ansible = True

        if host_via_api and value_is_ansible:

            hostname = result['host']
            hostid= result['hostid']
            for interface in result['interfaces']:

                interfaceid = interface["interfaceid"]
                ip = interface["ip"]
        device_dict = {"ip": ip, "hostid": hostid, "hostname": hostname, "interfaceid":interfaceid }


        device_list.append(device_dict)
    return device_list

device_list_for_maps = create_device(result)

for _ in device_list_for_maps:
    print(_)

hostid1 = device_list_for_maps[0]["hostid"]
hostid2 = device_list_for_maps[1]["hostid"] 


create_map = {
    "jsonrpc": "2.0",
    "method": "map.create",
    "params": {
        "name": "LAN",
        "width": 1920,
        "height": 1080,
        "label_type": 0,
        "label_type_host": 0,
        "label_type_hostgroup": 0,
        "label_type_image": 0,
        "label_type_map": 0,
        "label_type_trigger": 0,
        "selements": [
            {
                "selementid": "1",
                "elements": [
                    {"hostid": hostid1}
                ],
                "elementtype": 0,
                "iconid_off": "188",
                "label": "{HOST.CONN}\r\n{HOST.NAME}\r\n--------------------------\r\nOther information:",
                "width": "200",
                "x": "113",
                "y": "318",
                "tags": [
                    {
                        "operator": "0",
                        "tag": "api_platform",
                        "value": "cisco_ios"
                    }
                ],
            },
            {
                "selementid": "2",
                "elements": [
                    {"hostid": hostid2}
                ],
                "elementtype": 0,
                "iconid_off": "129",
                "label": "{HOST.NAME}\r\n{HOST.CONN}",
                "tags": [
                    {
                        "operator": "0",
                        "tag": "api_platform",
                        "value": "cisco_ios"
                    }
                ],
                "urls": [],
                "use_iconmap": "0",
                "viewtype": "0",
                "width": "200",
                "x": "563",
                "y": "318"
            }
        ],
        "links": [
            {
                "selementid1": "1",
                "selementid2": "2"
            }
        ]
    },
    "id": 1,
    "auth": AUTHTOKEN
}

req = requests.post(ZABBIX_API_URL, json = create_map , verify=False)
print(json.dumps(req.json(), sort_keys=True, indent=4))

result = req.json()["result"]
if result != "":
    print(f"\The map '{create_map['params']['name']}' was added successfully! ")
    print (result)
else:
    # create entry in error.log
    pass


req = requests.post(ZABBIX_API_URL,
                  json={
                      "jsonrpc": "2.0",
                      "method": "user.logout",
                      "params": {},
                      "id": 1,
                      "auth": AUTHTOKEN
                  }, verify=False)

print(json.dumps(req.json(), sort_keys=True, indent=4))