#!/usr/bin/python

# Create Devices in Zabbix Server via APIs:

import requests
import json
import urllib3
from datetime import datetime


urllib3.disable_warnings()

# Create device from list
def create_map(device_list_from_ansible, first_device_hostname):
    
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

    check_if_map_exist = {
    "jsonrpc": "2.0",
    "method": "map.get",
    "params": {
        "output": "extend",
        "selectSelements": "extend"
    },
    "id": 2,
    "auth": AUTHTOKEN
    }

    maps = requests.post(ZABBIX_API_URL, json = check_if_map_exist , verify=False)

    # if this map already exist
    map_exist = False

    # if exist take sysmapid
    for map in maps.json()["result"]:
        if  map['name'] == "LAN2":
            sysmapid = map['sysmapid'] 
            map_exist = True
            break
    
    # if this map does not exist create one
    if map_exist == False:
        # create empty map
        create_map = {
                "jsonrpc": "2.0",
                "method": "map.create",
                "params": {
                    "name": "LAN2",
                    "width": 1920,
                    "height": 1080
                },
                "id": 2,
                "auth": AUTHTOKEN
        }

        req = requests.post(ZABBIX_API_URL, json = create_map , verify=False)

        result = req.json()["result"]
        if result != "":
            print(f"\nThe map '{create_map['params']['name']}' was added successfully! ")

        else:
            # create entry in error.log
            pass
        
        # after new maps is created you need to find sysmapid
        check_if_map_exist = {
            "jsonrpc": "2.0",
            "method": "map.get",
            "params": {
                "output": "extend",
                "selectSelements": "extend"
            },
            "id": 2,
            "auth": AUTHTOKEN
            }

        maps = requests.post(ZABBIX_API_URL, json = check_if_map_exist , verify=False)

        # if exist take sysmapid
        for map in maps.json()["result"]:

            if  map['name'] == "LAN2":
                sysmapid = map['sysmapid'] 
                break

    # find hostid on the first host
    for device_zabbix in device_list_for_maps:
        if device_zabbix['hostname'] == first_device_hostname:
            hostid1 = device_zabbix['hostid']

    # create hostid for neighbour


    selementid1 = 1
    selementid2 = 2
    x2 = 560
    y2 = 320
    x1 = 113
    y1 = 320

    links = []

    # Create first host
    selements = [
    {
        "selementid": selementid1,
        "elements": [
            {"hostid": hostid1}
        ],
        "elementtype": 0,
        "iconid_off": "188",
        "label": "{HOST.CONN}\r\n{HOST.NAME}\r\n--------------------------\r\nOther information:",
        "width": "200",
        "x": x1,
        "y": y1,
        "tags": [
            {
                "operator": "0",
                "tag": "api_platform",
                "value": "cisco_ios"
            }
        ],
    }]

    # for all neighbours create links 
    # first check for dummy devices
    for device_ansible in device_list_from_ansible:
        if device_ansible['dummy_device'] == 'yes':
            pass
            #print(device_ansible)

        # Create links for directly connected hosts
        else:
            for device_zabbix in device_list_for_maps:

                # if device is already added to zabbix and match with ansibl 
                if device_zabbix['hostname'] == device_ansible['neighbour']:

                    # take hsotid for second device 
                    hostid2 = device_zabbix["hostid"] 
                    
                    selements.append(
                        {
                            "selementid": selementid2,
                            "elements": [
                                {"hostid": hostid2}
                            ],
                            "elementtype": 0,
                            "iconid_off": "129",
                            "label": "{HOST.CONN}\r\n{HOST.NAME}\r\n--------------------------\r\nOther information:",
                            "width": "200",
                            "x": x2,
                            "y": y2,
                            "tags": [
                                {
                                    "operator": "0",
                                    "tag": "api_platform",
                                    "value": "cisco_ios"
                                }
                            ],
                        })
                    
                    links.append({
                        "selementid1": selementid1,
                        "selementid2": selementid2
                    })

                    # increase selementsid for every devices
                    selementid2 += 1
                    x2 += 120
                    y2 += 120

    # for s in selements:
    #     print(s)

    update_map = {
        "jsonrpc": "2.0",
        "method": "map.update",
        "params": {
            "name": "LAN2",
            "width": 1920,
            "height": 1080,
            "sysmapid": sysmapid,
            "label_type": 0,
            "label_type_host": 0,
            "label_type_hostgroup": 0,
            "label_type_image": 0,
            "label_type_map": 0,
            "label_type_trigger": 0,
            "selements": selements,
            "links": links
        },
        "id": 1,
        "auth": AUTHTOKEN
    }

    

    req = requests.post(ZABBIX_API_URL, json = update_map , verify=False)
    #print(json.dumps(req.json(), sort_keys=True, indent=4))

    result = req.json()["result"]
    if result != "":
        print(f"\nThe map '{update_map['params']['name']}' was updated successfully! ")

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

device_list_from_ansible = [{'local_interface': 'GigabitEthernet0/3', 'neighbour': 'RB931-2nD', 'platform': 'MikroTik', 'port': 'Bridge-VxLAN-VNI-81/VxLAN-VNI', 'dummy_device': 'yes'},
{'local_interface': 'GigabitEthernet0/3', 'neighbour': 'RB4011iGS', 'platform': 'MikroTik', 'port': 'Bridge-VxLAN-VNI-81/LAB02-INF', 'dummy_device': 'yes'},
{'local_interface': 'GigabitEthernet0/3', 'neighbour': 'vios-2.vtechnology.eu', 'platform': 'Cisco ', 'port': 'GigabitEthernet0/2', 'dummy_device': 'yes'},
{'local_interface': 'GigabitEthernet0/3', 'neighbour': 'vios-3.vtechnology.eu', 'platform': 'Cisco ', 'port': 'GigabitEthernet0/1', 'dummy_device': 'yes'},
{'local_interface': 'GigabitEthernet0/0', 'neighbour': 'vios-2.vtechnology.eu', 'platform': 'Cisco ', 'port': 'GigabitEthernet0/1', 'dummy_device': 'no'},
{'local_interface': 'GigabitEthernet0/1', 'neighbour': 'vios-3.vtechnology.eu', 'platform': 'Cisco ', 'port': 'GigabitEthernet0/0', 'dummy_device': 'no'}]

first_device_hostname = 'vios1'

create_map(device_list_from_ansible,first_device_hostname)
