from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}


for device in (nxos1, nxos2):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show version")

    with open(device['host'] + "_show_version.txt", "w") as f:
       f.write(output)

    net_connect.disconnect()
