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
    import socket
    import requests
    from urllib.parse import urlparse
    import concurrent.futures
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Website Port Scanner")

# Global variable for thread synchronization
print_lock = threading.Lock()

def get_domain_info(url):
    """Extract domain from URL"""
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if not domain:
            domain = parsed_url.path
        
        # Remove port if present
        domain = domain.split(':')[0]
        
        # Remove www prefix
        if domain.startswith('www.'):
            domain = domain[4:]
            
        return domain
    except:
        return url

def get_ip_address(domain):
    """Get IP address of a domain"""
    try:
        return socket.gethostbyname(domain)
    except:
        return "Unknown"

def scan_port(ip, port, timeout=1):
    """Scan a single port"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        
        if result == 0:
            return port, True
        else:
            return port, False
    except:
        return port, False

def get_service_name(port):
    """Get common service name for port"""
    common_services = {
        21: 'FTP',
        22: 'SSH',
        23: 'Telnet',
        25: 'SMTP',
        53: 'DNS',
        80: 'HTTP',
        110: 'POP3',
        143: 'IMAP',
        443: 'HTTPS',
        465: 'SMTPS',
        587: 'SMTP Submission',
        993: 'IMAPS',
        995: 'POP3S',
        2082: 'cPanel',
        2083: 'cPanel SSL',
        2086: 'WHM',
        2087: 'WHM SSL',
        2095: 'Webmail',
        2096: 'Webmail SSL',
        3306: 'MySQL',
        5432: 'PostgreSQL',
        8080: 'HTTP Proxy',
        8443: 'HTTPS Alternative',
        8888: 'Jupyter',
        9000: 'PHP-FPM',
        10000: 'Webmin',
        27017: 'MongoDB',
    }
    
    return common_services.get(port, 'Unknown')

def scan_web_ports(ip):
    """Scan common web-related ports"""
    open_ports = []
    
    # Common web ports
    web_ports = [
        # HTTP/HTTPS
        80, 443, 8080, 8443, 8000, 3000, 5000,
        # Control Panels
        2082, 2083, 2086, 2087, 2095, 2096, 10000,
        # Development
        3000, 4200, 5000, 8000, 8080, 8888, 9000,
        # Common Alternative Ports
        81, 82, 83, 84, 85, 86, 87, 88, 89,
        444, 445, 9443, 7443,
        # HTTP Alt
        8008, 8081, 8088, 8090, 8181, 8282, 8383, 8484, 8585,
        # HTTPS Alt
        9443, 9543, 9643, 9743, 9843, 9943
    ]
    
    # Use threading for faster port scanning
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_port = {executor.submit(scan_port, ip, port, 1): port for port in web_ports}
        
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
            try:
                port_num, is_open = future.result()
                if is_open:
                    service = get_service_name(port_num)
                    open_ports.append((port_num, service))
            except Exception:
                pass
    
    return open_ports

def get_website_name(url):
    """Get website name/title"""
    try:
        # Try to get the website title
        if not url.startswith(('http://', 'https://')):
            test_url = 'https://' + url
        else:
            test_url = url
        
        response = requests.get(test_url, timeout=5, allow_redirects=True)
        response.raise_for_status()
        
        # Try to find title in HTML
        html = response.text.lower()
        
        # Look for title tag
        title_start = html.find('<title>')
        if title_start != -1:
            title_start += 7
            title_end = html.find('</title>', title_start)
            if title_end != -1:
                title = html[title_start:title_end].strip()
                if title:
                    # Capitalize first letter of each word
                    title = ' '.join(word.capitalize() for word in title.split())
                    return title
        
        # If no title found, use domain as fallback
        domain = get_domain_info(url)
        return domain.capitalize()
        
    except requests.exceptions.SSLError:
        # Try without SSL
        try:
            if url.startswith('https://'):
                http_url = url.replace('https://', 'http://')
                response = requests.get(http_url, timeout=5, allow_redirects=True)
                html = response.text.lower()
                
                title_start = html.find('<title>')
                if title_start != -1:
                    title_start += 7
                    title_end = html.find('</title>', title_start)
                    if title_end != -1:
                        title = html[title_start:title_end].strip()
                        if title:
                            title = ' '.join(word.capitalize() for word in title.split())
                            return title + " (HTTP)"
        except:
            pass
        
    except:
        pass
    
    # Final fallback
    domain = get_domain_info(url)
    return domain.capitalize()

def scan_website_info(url):
    """Main function to scan website information"""
    info = {}
    info['original_url'] = url
    
    # Get domain
    domain = get_domain_info(url)
    info['domain'] = domain
    
    # Get IP address
    ip = get_ip_address(domain)
    info['ip_address'] = ip
    
    # Get website name/title
    website_name = get_website_name(url)
    info['website_name'] = website_name
    
    # Scan ports
    info['open_ports'] = scan_web_ports(ip)
    
    return info

def display_simple_results(info):
    """Display the scan results in a simple format"""
    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Website Information:")
    print(f"{white}─" * 50 + reset)
    
    # Website Name
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO_ADD} Website Name : {white}{info['website_name']}{red}")
    
    # Domain
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO_ADD} Domain       : {white}{info['domain']}{red}")
    
    # IP Address
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO_ADD} IP Address   : {white}{info['ip_address']}{red}")
    
    # Open Ports
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO_ADD} Open Ports   :")
    
    open_ports = info['open_ports']
    if open_ports:
        for port, service in open_ports:
            print(f"              {white}{port:<6} - {service}{red}")
    else:
        print(f"              {white}No open web ports found{red}")

try:
    Slow(map_banner)
    
    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Simple Website Port Scanner")
    print(f"{white}─" * 50 + reset)
    
    # Get website URL from user
    print(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Enter website URL (e.g., example.com):")
    website_url = input(f"{color.RED}  {color.WHITE}>> {color.RESET}").strip()
    
    if not website_url:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} No URL provided!")
    else:
        print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Scanning website...")
        
        # Scan the website
        website_info = scan_website_info(website_url)
        
        # Display results
        display_simple_results(website_info)
    
    print(f"\n{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}")

    Continue()
    Reset()
except KeyboardInterrupt:
    print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR} Scan interrupted by user.")
    Continue()
    Reset()
except Exception as e:
    Error(e)
