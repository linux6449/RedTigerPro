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

print_lock = threading.Lock()

def get_domain_info(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if not domain:
            domain = parsed_url.path
        
        domain = domain.split(':')[0]
        
        if domain.startswith('www.'):
            domain = domain[4:]
            
        return domain
    except:
        return url

def get_ip_address(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return "Unknown"

def scan_port(ip, port, timeout=1):
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
    open_ports = []
    
    web_ports = [
        80, 443, 8080, 8443, 8000, 3000, 5000,
        2082, 2083, 2086, 2087, 2095, 2096, 10000,
        3000, 4200, 5000, 8000, 8080, 8888, 9000,
        81, 82, 83, 84, 85, 86, 87, 88, 89,
        444, 445, 9443, 7443,
        8008, 8081, 8088, 8090, 8181, 8282, 8383, 8484, 8585,
        9443, 9543, 9643, 9743, 9843, 9943
    ]
    
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
    try:
        if not url.startswith(('http://', 'https://')):
            test_url = 'https://' + url
        else:
            test_url = url
        
        response = requests.get(test_url, timeout=5, allow_redirects=True)
        response.raise_for_status()
        
        html = response.text.lower()
        
        title_start = html.find('<title>')
        if title_start != -1:
            title_start += 7
            title_end = html.find('</title>', title_start)
            if title_end != -1:
                title = html[title_start:title_end].strip()
                if title:
                    title = ' '.join(word.capitalize() for word in title.split())
                    return title
        
        domain = get_domain_info(url)
        return domain.capitalize()
        
    except requests.exceptions.SSLError:
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
    
    domain = get_domain_info(url)
    return domain.capitalize()

def scan_website_info(url):
    info = {}
    info['original_url'] = url
    
    domain = get_domain_info(url)
    info['domain'] = domain
    
    ip = get_ip_address(domain)
    info['ip_address'] = ip
    
    website_name = get_website_name(url)
    info['website_name'] = website_name
    
    info['open_ports'] = scan_web_ports(ip)
    
    return info

def display_simple_results(info):
    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Website Information:")
    print(f"{white}─" * 50 + reset)
    
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO_ADD} Website Name : {white}{info['website_name']}{red}")
    
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO_ADD} Domain       : {white}{info['domain']}{red}")
    
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO_ADD} IP Address   : {white}{info['ip_address']}{red}")
    
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
    
    print(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Enter website URL (e.g., example.com):")
    website_url = input(f"{color.RED}  {color.WHITE}>> {color.RESET}").strip()
    
    if not website_url:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} No URL provided!")
    else:
        print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Scanning website...")
        
        website_info = scan_website_info(website_url)
        
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