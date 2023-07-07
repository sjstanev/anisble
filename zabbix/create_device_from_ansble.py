import json
import method_create_list_of_neigbours as mcln
import method_create_device as mcd
import method_get_hosts as mgh


"""
To create a host you must have following data:

host_name = "vois2"
ip_addr = "10.81.0.235"
platform = "cisco_ios"

all data is received via ansible script

"""


# Create first device in zabbix
def create_single_device(result):
    # create hostname var
    hostname = result["ansible_facts"]["ansible_net_hostname"]
    first_device_hostname = hostname

    # create ip_addr var
    if len(result["ansible_facts"]["ansible_net_all_ipv4_addresses"]) > 1:
        ip_addr = result["ansible_facts"]["ansible_net_all_ipv4_addresses"][1]
    else:
        ip_addr = result["ansible_facts"]["ansible_net_all_ipv4_addresses"][0]

    # create platform var
    platform = "cisco"

    # check whether host exist in zabbix
    zhost = zabbix_hosts_exist(zabbix_hosts,hostname)

    # add only unique host
    if zhost == False:
        # Create device using ansible results
        mcd.create_single_devic_via_ansible(hostname, ip_addr, platform)
    else:
        print(f'The {hostname} is already added to zabbix!')

    return(first_device_hostname) 



# Create other devices in zabbix
def create_multiple_host(neighbours_list,zabbix_hosts):

    #empty list with neighbours
    unique_neighbour = []
    counter = 0
    for neighbour in neighbours_list:
        counter += 1

        # [int, neihbour["host"], neihbour["platform"], neihbour["port"]])
        hostname = neighbour['neighbour']
        platform = neighbour['platform']
        ip_addrs = f'10.10.10.{counter}'

        # check whether host exist in zabbix
        zhost = zabbix_hosts_exist(zabbix_hosts,hostname)

        # apeend only unique host
        if hostname not in unique_neighbour and zhost == False:
            # create list with unique host
            unique_neighbour.append(hostname)

            # add host to zabbix
            mcd.create_multiple_devic_via_ansible(hostname, ip_addrs, platform)
        else:
            print(f'The {hostname} is already added to zabbix!')


# check whether host exist in zabbix
def zabbix_hosts_exist(zabbix_hosts,hostname):
    for zhost in zabbix_hosts:

        # device exist continue
        if hostname in  zhost['host']:
            return True
            break
    return False


# results from ansible check
output = '{"ansible_facts": {"ansible_network_resources": {}, "ansible_net_gather_network_resources": [], "ansible_net_gather_subset": ["default", "hardware", "interfaces"], "ansible_net_system": "ios", "ansible_net_model": "IOSv", "ansible_net_image": "flash0:/vios_l2-adventerprisek9-m", "ansible_net_version": "15.2(CML_NIGHTLY_20180619)FLO_DSGS7", "ansible_net_hostname": "vios1", "ansible_net_api": "cliconf", "ansible_net_python_version": "3.9.2", "ansible_net_iostype": "IOS", "ansible_net_serialnum": "9321SXL6F4H", "ansible_net_filesystems": ["flash0:"], "ansible_net_filesystems_info": {"flash0:": {"spacetotal_kb": 2092496.0, "spacefree_kb": 1971128.0}}, "ansible_net_memtotal_mb": 336988.6875, "ansible_net_memfree_mb": 235193.12890625, "ansible_net_all_ipv4_addresses": ["10.10.10.1", "10.81.0.234"], "ansible_net_all_ipv6_addresses": [], "ansible_net_neighbors": {"GigabitEthernet0/3": [{"host": "RB931-2nD", "platform": "MikroTik", "port": "Bridge-VxLAN-VNI-81/VxLAN-VNI"}, {"host": "RB4011iGS", "platform": "MikroTik", "port": "Bridge-VxLAN-VNI-81/LAB02-INF"}, {"host": "vios-2.vtechnology.eu", "platform": "Cisco ", "port": "GigabitEthernet0/2"}, {"host": "vios-3.vtechnology.eu", "platform": "Cisco ", "port": "GigabitEthernet0/1"}], "GigabitEthernet0/0": [{"host": "vios-2.vtechnology.eu", "platform": "Cisco ", "port": "GigabitEthernet0/1"}], "GigabitEthernet0/1": [{"host": "vios-3.vtechnology.eu", "platform": "Cisco ", "port": "GigabitEthernet0/0"}]}, "ansible_net_interfaces": {"GigabitEthernet0/0": {"description": null, "macaddress": "0ca6.320f.0000", "mtu": 1500, "bandwidth": 1000000, "mediatype": "RJ45", "duplex": "Auto", "lineprotocol": "up", "operstatus": "up", "type": "iGbE", "ipv4": []}, "GigabitEthernet0/1": {"description": null, "macaddress": "0ca6.320f.0001", "mtu": 1500, "bandwidth": 1000000, "mediatype": "RJ45", "duplex": "Auto", "lineprotocol": "up", "operstatus": "up", "type": "iGbE", "ipv4": [{"address": "10.10.10.1", "subnet": "24"}]}, "GigabitEthernet0/2": {"description": null, "macaddress": "0ca6.320f.0002", "mtu": 1500, "bandwidth": 1000000, "mediatype": "RJ45", "duplex": "Auto", "lineprotocol": "down", "operstatus": "down", "type": "iGbE", "ipv4": []}, "GigabitEthernet0/3": {"description": null, "macaddress": "0ca6.320f.0003", "mtu": 1500, "bandwidth": 1000000, "mediatype": "RJ45", "duplex": "Auto", "lineprotocol": "up", "operstatus": "up", "type": "iGbE", "ipv4": [{"address": "10.81.0.234", "subnet": "24"}]}}}, "failed": false, "changed": false}'

# convert output to dict
result = json.loads(output)

# print only ansible_net_neighbors
net_neighbors = result["ansible_facts"]["ansible_net_neighbors"]

# Create list with number of neighbour on every interface
neighbours_list = mcln.network_neigbours(net_neighbors)
# for n in neighbours_list:
#     print(n)

# Gather information whether this device already exist in Zabbix
zabbix_hosts = mgh.get_host_via_api()

# Create first device in zabbix -- local def
first_device_hostname = create_single_device(result)
#print(first_device_hostname)

# Create other devices in zabbix -- local def
create_multiple_host(neighbours_list,zabbix_hosts)

