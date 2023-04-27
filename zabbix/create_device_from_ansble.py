import json
import user_login_logout as ll


"""
To create a host must have:

host_name = "vois2"
ip_addr = "10.81.0.235"
platform = "cisco_ios"

"""


output = '{"ansible_facts": {"ansible_network_resources": {}, "ansible_net_gather_network_resources": [], "ansible_net_gather_subset": ["default", "hardware", "interfaces"], "ansible_net_system": "ios", "ansible_net_model": "IOSv", "ansible_net_image": "flash0:/vios_l2-adventerprisek9-m", "ansible_net_version": "15.2(CML_NIGHTLY_20180619)FLO_DSGS7", "ansible_net_hostname": "vios1", "ansible_net_api": "cliconf", "ansible_net_python_version": "3.9.2", "ansible_net_iostype": "IOS", "ansible_net_serialnum": "9321SXL6F4H", "ansible_net_filesystems": ["flash0:"], "ansible_net_filesystems_info": {"flash0:": {"spacetotal_kb": 2092496.0, "spacefree_kb": 1971128.0}}, "ansible_net_memtotal_mb": 336988.6875, "ansible_net_memfree_mb": 235193.12890625, "ansible_net_all_ipv4_addresses": ["10.10.10.1", "10.81.0.234"], "ansible_net_all_ipv6_addresses": [], "ansible_net_neighbors": {"GigabitEthernet0/3": [{"host": "RB931-2nD", "platform": "MikroTik", "port": "Bridge-VxLAN-VNI-81/VxLAN-VNI"}, {"host": "RB4011iGS", "platform": "MikroTik", "port": "Bridge-VxLAN-VNI-81/LAB02-INF"}, {"host": "vios-2.vtechnology.eu", "platform": "Cisco ", "port": "GigabitEthernet0/2"}, {"host": "vios-3.vtechnology.eu", "platform": "Cisco ", "port": "GigabitEthernet0/1"}], "GigabitEthernet0/0": [{"host": "vios-2.vtechnology.eu", "platform": "Cisco ", "port": "GigabitEthernet0/1"}], "GigabitEthernet0/1": [{"host": "vios-3.vtechnology.eu", "platform": "Cisco ", "port": "GigabitEthernet0/0"}]}, "ansible_net_interfaces": {"GigabitEthernet0/0": {"description": null, "macaddress": "0ca6.320f.0000", "mtu": 1500, "bandwidth": 1000000, "mediatype": "RJ45", "duplex": "Auto", "lineprotocol": "up", "operstatus": "up", "type": "iGbE", "ipv4": []}, "GigabitEthernet0/1": {"description": null, "macaddress": "0ca6.320f.0001", "mtu": 1500, "bandwidth": 1000000, "mediatype": "RJ45", "duplex": "Auto", "lineprotocol": "up", "operstatus": "up", "type": "iGbE", "ipv4": [{"address": "10.10.10.1", "subnet": "24"}]}, "GigabitEthernet0/2": {"description": null, "macaddress": "0ca6.320f.0002", "mtu": 1500, "bandwidth": 1000000, "mediatype": "RJ45", "duplex": "Auto", "lineprotocol": "down", "operstatus": "down", "type": "iGbE", "ipv4": []}, "GigabitEthernet0/3": {"description": null, "macaddress": "0ca6.320f.0003", "mtu": 1500, "bandwidth": 1000000, "mediatype": "RJ45", "duplex": "Auto", "lineprotocol": "up", "operstatus": "up", "type": "iGbE", "ipv4": [{"address": "10.81.0.234", "subnet": "24"}]}}}, "failed": false, "changed": false}'

# convert output to dict
result = json.loads(output)

# print only ansible_net_neighbors
net_neighbors = result["ansible_facts"]["ansible_net_neighbors"]
# print(net_neighbors)
print('-' * 80)
for int,neihbours in net_neighbors.items():
    count_neighbours = len(neihbours)
    print(f'\nOn interface {int} there {count_neighbours} neighbour(s).')
    for neihbour in neihbours:
        print (f'interface {int} : neighbour { neihbour["host"] }, platform: {neihbour["platform"]}, port {neihbour["port"]}')

# convert dict to JSON

print("-" * 80)

hostname = result["ansible_facts"]["ansible_net_hostname"]
first_ip = result["ansible_facts"]["ansible_net_all_ipv4_addresses"][1]
platform = "cisco"

# Create device using ansible results
# user_login = ll.create_devic_via_ansible(hostname, first_ip, platform)

print("-" * 80)









### if want to see result in JSON
json_result = json.dumps(result, sort_keys=True, indent=4)
# print JSON format
print(json_result)



