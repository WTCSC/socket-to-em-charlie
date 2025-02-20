import psutil
import socket
def get_ip_addresses():
    ip_addresses = {}
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:  # IPv4 addresses only
                ip_addresses[interface] = addr.address
    return ip_addresses

ip_addresses = get_ip_addresses()
iplist = ["Select Adapter"] + [f"{interface}: {ip}" for interface, ip in ip_addresses.items()]
ipaddrlist = [ip for interface, ip in ip_addresses.items()]

selected = ipaddrlist[iplist.index(iplist[1])-1]
print(selected)
