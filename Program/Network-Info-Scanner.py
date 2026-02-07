# Copyright (c) RedTigerPro 
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Config.Util import *
from Config.Config import *
try:
    import requests
    import socket
    import netifaces
    import psutil
except Exception as e:
   ErrorModule(e)
   
Title("Network Info Scanner")

def get_local_ips():
    """Get all local IP addresses"""
    ips = []
    try:
        interfaces = netifaces.interfaces()
        for interface in interfaces:
            addrs = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addrs:
                for addr_info in addrs[netifaces.AF_INET]:
                    ip = addr_info.get('addr')
                    if ip and ip != '127.0.0.1':
                        ips.append(ip)
    except:
        pass
    
    # Fallback method if netifaces not available
    if not ips:
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            if local_ip != '127.0.0.1':
                ips.append(local_ip)
        except:
            pass
    
    return ips

def get_public_ip():
    """Get public IP address"""
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        if response.status_code == 200:
            return response.json().get('ip', 'Unknown')
    except:
        pass
    return 'Unknown'

def get_open_ports():
    """Get list of open ports on local machine"""
    open_ports = []
    try:
        connections = psutil.net_connections()
        for conn in connections:
            if conn.status == 'LISTEN':
                if conn.laddr:
                    port = conn.laddr.port
                    if port not in open_ports:
                        open_ports.append(port)
    except:
        pass
    
    # Common ports to check if psutil method fails
    if not open_ports:
        common_ports = [80, 443, 22, 21, 25, 53, 3306, 5432, 8080, 8443]
        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex(('127.0.0.1', port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
            except:
                pass
    
    return sorted(open_ports)[:20]  # Return first 20 ports max

def get_network_info():
    """Get comprehensive network information"""
    info = {}
    
    # Get local IPs
    info['local_ips'] = get_local_ips()
    
    # Get public IP
    info['public_ip'] = get_public_ip()
    
    # Get open ports
    info['open_ports'] = get_open_ports()
    
    # Get hostname
    try:
        info['hostname'] = socket.gethostname()
    except:
        info['hostname'] = 'Unknown'
    
    # Get network interfaces (simplified)
    info['interfaces'] = []
    try:
        interfaces = psutil.net_if_addrs()
        for interface_name, interface_addresses in interfaces.items():
            for address in interface_addresses:
                if address.family == socket.AF_INET:
                    info['interfaces'].append({
                        'name': interface_name,
                        'ip': address.address,
                        'netmask': address.netmask
                    })
    except:
        pass
    
    return info

try:
    Slow(map_banner)
    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Scanning network information...")
    
    network_info = get_network_info()
    
    # Display results
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO_ADD} Hostname   : {white}{network_info.get('hostname', 'Unknown')}{red}")
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO_ADD} Public IP  : {white}{network_info.get('public_ip', 'Unknown')}{red}")
    
    # Display local IPs
    local_ips = network_info.get('local_ips', [])
    if local_ips:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO_ADD} Local IPs  :")
        for ip in local_ips:
            print(f"              {white}{ip}{red}")
    else:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO_ADD} Local IPs  : {white}None found{red}")
    
    # Display network interfaces
    interfaces = network_info.get('interfaces', [])
    if interfaces:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO_ADD} Interfaces :")
        for iface in interfaces[:3]:  # Show first 3 interfaces
            print(f"              {white}{iface.get('name', 'Unknown')}: {iface.get('ip', 'Unknown')} (Mask: {iface.get('netmask', 'Unknown')}){red}")
    
    # Display open ports
    open_ports = network_info.get('open_ports', [])
    if open_ports:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO_ADD} Open Ports :")
        ports_str = ', '.join(str(port) for port in open_ports)
        # Split long port list into multiple lines
        max_line_length = 60
        current_line = ""
        for port in ports_str.split(', '):
            if len(current_line) + len(port) + 2 > max_line_length:
                print(f"              {white}{current_line}{red}")
                current_line = port
            else:
                if current_line:
                    current_line += ", " + port
                else:
                    current_line = port
        if current_line:
            print(f"              {white}{current_line}{red}")
    else:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO_ADD} Open Ports : {white}None found or accessible{red}")
    
    print(f"\n{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}")

    Continue()
    Reset()
except Exception as e:
    Error(e)