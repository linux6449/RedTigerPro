# Copyright (c) RedTigerPro 
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

import socket
import concurrent.futures
import requests
from urllib.parse import urlparse
import ssl
import urllib3
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import sys
import os
import time
from datetime import datetime


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

BEFORE = f"{Colors.CYAN}[{Colors.RESET}"
AFTER = f"{Colors.CYAN}]{Colors.RESET}"
ADD = f"{Colors.GREEN}+{Colors.RESET}"
INFO = f"{Colors.BLUE}i{Colors.RESET}"
INPUT = f"{Colors.YELLOW}?{Colors.RESET}"
WAIT = f"{Colors.MAGENTA}~{Colors.RESET}"
ERROR = f"{Colors.RED}!{Colors.RESET}"
WHITE = Colors.WHITE
red = Colors.RED
reset = Colors.RESET

def current_time_hour():
    return datetime.now().strftime('%H:%M:%S')

def Title(title):
    os.system('clear' if os.name == 'posix' else 'cls')
    banner = f"""{Colors.CYAN}
╔═╗╔═╗╔╗ ╦ ╦╦╔═╗  ╔═╗ ╔═╗╔═╗╔╦╗╦╔═╗╔╗╔
╠═╣╠═╝╠╩╗║ ║║║ ║  ╠═╝ ║ ║╠═╝ ║ ║║ ║║║║
╩ ╩╩  ╚═╝╚═╝╩╚═╝  ╩   ╚═╝╩   ╩ ╩╚═╝╝╚╝
{Colors.RESET}{'='*60}
{Colors.BOLD}{title}{Colors.RESET}
{'='*60}"""
    print(banner)

def ChoiceUserAgent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ]
    return user_agents[0]

def Error(e):
    print(f"\n{ERROR} {Colors.RED}Error: {e}{Colors.RESET}")
    input(f"\n{INFO} Press Enter to exit...")
    sys.exit(1)

def ErrorModule(e):
    print(f"{ERROR} {Colors.RED}Missing module: {e}{Colors.RESET}")
    print(f"{INFO} Install it with: pip install {str(e).split()[-1]}")
    sys.exit(1)

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

def Censored(text):
    return '*' * len(text) if len(text) > 3 else '***'

def Continue():
    input(f"\n{INFO} Press Enter to continue...")

def Reset():
    Title("Website Scanner - Reset")
    print(f"{INFO} {Colors.GREEN}Scanner has been reset{Colors.RESET}")

def WebsiteFoundUrl(url):
    if not urlparse(url).scheme:
        website_url = f"https://{url}"
    else:
        website_url = url
    print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} Website: {WHITE}{website_url}{red}")
    return website_url

def WebsiteDomain(website_url):
    domain = urlparse(website_url).netloc
    print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} Domain: {WHITE}{domain}{red}")
    return domain

def WebsiteIp(domain):
    try:
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        ip = "None"
    if ip != "None":
        print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} IP: {WHITE}{ip}{red}")
    else:
        print(f"{BEFORE}{current_time_hour()}{AFTER} {ERROR} IP: {WHITE}Could not resolve{red}")
    return ip

def IpType(ip):
    if ip == "None":
        return
    if ':' in ip:
        type_ip = "IPv6" 
    elif '.' in ip:
        type_ip = "IPv4"
    else:
        type_ip = "Unknown"
    print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} IP Type: {WHITE}{type_ip}{red}")

def WebsiteSecure(website_url):
    is_secure = website_url.startswith('https://')
    color = Colors.GREEN if is_secure else Colors.RED
    status = "Yes" if is_secure else "No"
    print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} Secure (HTTPS): {color}{status}{red}")

def WebsiteStatus(website_url):
    try:
        response = requests.get(website_url, timeout=5, headers={"User-Agent": ChoiceUserAgent()}, verify=False)
        status_code = response.status_code
    except RequestException:
        status_code = 404
    
    if 200 <= status_code < 300:
        color = Colors.GREEN
    elif 300 <= status_code < 400:
        color = Colors.YELLOW
    else:
        color = Colors.RED
        
    print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} Status Code: {color}{status_code}{red}")

def IpInfo(ip):
    if ip == "None":
        print(f"{BEFORE}{current_time_hour()}{AFTER} {INFO} IP Info: {WHITE}No IP available{red}")
        return
    
    try:
        api = requests.get(f"https://ipinfo.io/{ip}/json", headers={"User-Agent": ChoiceUserAgent()}, timeout=5).json()
    except RequestException:
        api = {}
    
    if 'error' in api:
        print(f"{BEFORE}{current_time_hour()}{AFTER} {INFO} IP Info: {WHITE}API limit reached or error{red}")
        return
    
    info_keys = {
        'country': 'Country',
        'hostname': 'Hostname', 
        'isp': 'ISP',
        'org': 'Organization',
        'asn': 'ASN'
    }
    
    for key, display_name in info_keys.items():
        if key in api and api[key]:
            print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} {display_name}: {WHITE}{api[key]}{red}")

def IpDns(ip):
    if ip == "None":
        return
        
    try:
        dns = socket.gethostbyaddr(ip)[0]
    except:
        dns = "None"
    
    if dns != "None":
        print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} Host DNS: {WHITE}{dns}{red}")

def WebsitePort(ip):
    if ip == "None":
        print(f"{BEFORE}{current_time_hour()}{AFTER} {INFO} Port Scan: {WHITE}No IP available{red}")
        return
    
    ports = [21, 22, 23, 25, 53, 69, 80, 110, 123, 143, 194, 389, 443, 161, 3306, 5432, 6379, 1521, 3389]
    port_protocol_map = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
        80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
        443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
        1521: "Oracle DB", 3389: "RDP"
    }
    
    dangerous_ports = [23, 161, 3389, 1433, 5900]
    
    open_ports = []

    def ScanPort(ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                if sock.connect_ex((ip, port)) == 0:
                    protocol = port_protocol_map.get(port, 'Unknown')
                    status = "Open"
                    
                    if port in dangerous_ports:
                        status = f"{Colors.RED}Open (DANGEROUS){Colors.RESET}"
                    
                    open_ports.append((port, protocol, status))
        except:
            pass

    print(f"{BEFORE}{current_time_hour()}{AFTER} {WAIT} Scanning ports...{reset}")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(lambda p: ScanPort(ip, p), ports)
    
    if open_ports:
        for port, protocol, status in open_ports:
            print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} Port: {WHITE}{port}{red} Status: {status}{red} Protocol: {WHITE}{protocol}{red}")
    else:
        print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} No open ports found{red}")

def HttpHeaders(website_url):
    try:
        response = requests.get(website_url, timeout=5, headers={"User-Agent": ChoiceUserAgent()}, verify=False)
        headers = response.headers
        
        important_headers = ['Server', 'X-Powered-By', 'Content-Type', 'Content-Length', 'Date', 'Connection']
        
        for header in important_headers:
            if header in headers:
                value = headers[header]
                if header == 'Server':
                    old_servers = ['Apache/2.2', 'nginx/1.10', 'IIS/6.0', 'IIS/7.0']
                    for old_server in old_servers:
                        if old_server in value:
                            value = f"{Colors.RED}{value} (OLD VERSION){Colors.RESET}"
                            break
                print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} HTTP Header: {WHITE}{header}{red} Value: {WHITE}{value}{red}")
    except RequestException:
        print(f"{BEFORE}{current_time_hour()}{AFTER} {ERROR} Could not retrieve HTTP headers{red}")

def CheckSslCertificate(website_url):
    if not website_url.startswith('https://'):
        print(f"{BEFORE}{current_time_hour()}{AFTER} {INFO} SSL: {WHITE}Not using HTTPS{red}")
        return
    
    try:
        domain = urlparse(website_url).hostname
        context = ssl.create_default_context()
        
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

                issuer = dict(x[0] for x in cert['issuer'])
                print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} SSL Issuer: {WHITE}{issuer.get('organizationName', 'Unknown')}{red}")

                not_after = cert['notAfter']
                print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} SSL Valid Until: {WHITE}{not_after}{red}")

                expire_date = datetime.strptime(not_after, '%b %d %H:%M:%S %Y %Z')
                days_to_expire = (expire_date - datetime.now()).days
                
                if days_to_expire < 30:
                    print(f"{BEFORE}{current_time_hour()}{AFTER} {ERROR} SSL Certificate: {WHITE}Expires in {days_to_expire} days!{red}")
                
    except Exception as e:
        print(f"{BEFORE}{current_time_hour()}{AFTER} {ERROR} SSL Check Failed: {WHITE}{str(e)}{red}")

def CheckSecurityHeaders(website_url):
    security_headers = {
        'Content-Security-Policy': 'Protects against XSS attacks',
        'Strict-Transport-Security': 'Forces HTTPS connections',
        'X-Content-Type-Options': 'Prevents MIME type sniffing',
        'X-Frame-Options': 'Protects against clickjacking',
        'X-XSS-Protection': 'Basic XSS protection'
    }
    
    try:
        response = requests.get(website_url, timeout=5, headers={"User-Agent": ChoiceUserAgent()}, verify=False)
        response_headers = response.headers
        
        for header, description in security_headers.items():
            if header in response_headers:
                print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} Security Header: {Colors.GREEN}{header}{red} - {WHITE}Present{red}")
            else:
                print(f"{BEFORE}{current_time_hour()}{AFTER} {ERROR} Missing Security Header: {Colors.RED}{header}{red} - {WHITE}{description}{red}")
    except RequestException:
        print(f"{BEFORE}{current_time_hour()}{AFTER} {ERROR} Could not check security headers{red}")

def AnalyzeCookies(website_url):
    try:
        response = requests.get(website_url, timeout=5, headers={"User-Agent": ChoiceUserAgent()}, verify=False)
        cookies = response.cookies
        
        if not cookies:
            print(f"{BEFORE}{current_time_hour()}{AFTER} {INFO} No cookies found{red}")
            return
        
        security_issues = []
        
        for cookie in cookies:
            secure = 'Secure' if cookie.secure else 'Not Secure'
            httponly = 'HttpOnly' if cookie.has_nonstandard_attr('HttpOnly') else 'Not HttpOnly'

            if not cookie.secure:
                security_issues.append(f"Cookie '{cookie.name}' is not Secure")
            if not cookie.has_nonstandard_attr('HttpOnly'):
                security_issues.append(f"Cookie '{cookie.name}' is not HttpOnly")
            
            print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} Cookie: {WHITE}{cookie.name}{red} Secure: {WHITE}{secure}{red} HttpOnly: {WHITE}{httponly}{red}")
        
        if security_issues:
            print(f"\n{BEFORE}{current_time_hour()}{AFTER} {ERROR} Security Issues Found:{red}")
            for issue in security_issues:
                print(f"{BEFORE}{current_time_hour()}{AFTER} {ERROR} {WHITE}{issue}{red}")
                
    except RequestException:
        print(f"{BEFORE}{current_time_hour()}{AFTER} {ERROR} Could not analyze cookies{red}")

def DetectTechnologies(website_url):
    try:
        response = requests.get(website_url, timeout=5, headers={"User-Agent": ChoiceUserAgent()}, verify=False)
        headers = response.headers
        soup = BeautifulSoup(response.content, 'html.parser')
        
        technologies = []

        if 'server' in headers:
            server = headers['server']
            technologies.append(f"Server: {server}")

            old_indicators = ['Apache/2.2', 'nginx/1.10', 'IIS/6.0', 'IIS/7.0', 'Microsoft-IIS/8.0']
            for indicator in old_indicators:
                if indicator in server:
                    technologies.append(f"{Colors.RED}Warning: Old server version detected{Colors.RESET}")

        if 'x-powered-by' in headers:
            technologies.append(f"Powered By: {headers['x-powered-by']}")
        
        html_content = str(soup).lower()
        
        framework_indicators = {
            'wordpress': ['wp-content', 'wordpress'],
            'joomla': ['joomla', 'com_content'],
            'drupal': ['drupal', 'sites/all'],
            'laravel': ['laravel', 'csrf-token'],
            'django': ['django', 'csrfmiddlewaretoken'],
            'react': ['react', 'react-dom'],
            'angular': ['ng-', 'angular'],
            'vue': ['vue', 'vue.js'],
            'jquery': ['jquery'],
            'bootstrap': ['bootstrap']
        }
        
        for framework, indicators in framework_indicators.items():
            for indicator in indicators:
                if indicator in html_content:
                    technologies.append(f"Framework: {framework.capitalize()}")
                    break

        for script in soup.find_all('script', src=True):
            src = script['src'].lower()
            if 'jquery' in src:
                technologies.append("JavaScript: jQuery")
            if 'bootstrap' in src:
                technologies.append("CSS: Bootstrap")
        
        if technologies:
            for tech in set(technologies):  # set a duplikációk elkerülésére
                print(f"{BEFORE}{current_time_hour()}{AFTER} {ADD} Technology: {WHITE}{tech}{red}")
        else:
            print(f"{BEFORE}{current_time_hour()}{AFTER} {INFO} No technologies detected{red}")
            
    except Exception as e:
        print(f"{BEFORE}{current_time_hour()}{AFTER} {ERROR} Technology detection failed: {WHITE}{str(e)}{red}")

def main():
    try:
        Title("Website Scanner")
        
        user_agent = ChoiceUserAgent()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        scan_banner = f"""
{Colors.CYAN}Starting comprehensive website security scan...
This tool will check:{Colors.RESET}
{Colors.WHITE}• DNS and IP Information
• Port Security
• SSL/TLS Certificates
• HTTP Headers
• Security Headers
• Cookies Security
• Web Technologies{Colors.RESET}
"""
        Slow(scan_banner)
        print(f"{BEFORE}{current_time_hour()}{AFTER} {INFO} Selected User-Agent: {WHITE}{user_agent}{red}")
        
        url = input(f"{BEFORE}{current_time_hour()}{AFTER} {INPUT} Website URL -> {reset}").strip()
        
        if not url:
            print(f"{BEFORE}{current_time_hour()}{AFTER} {ERROR} No URL provided!{red}")
            Continue()
            return
        
        print(f"\n{BEFORE}{current_time_hour()}{AFTER} {WAIT} Scanning {WHITE}{url}{red}...{reset}")
        print(f"{BEFORE}{current_time_hour()}{AFTER} {INFO} Censored input: {WHITE}{Censored(url)}{red}\n")
        
        website_url = WebsiteFoundUrl(url)
        domain = WebsiteDomain(website_url)
        ip = WebsiteIp(domain)
        IpType(ip)
        WebsiteSecure(website_url)
        WebsiteStatus(website_url)
        IpInfo(ip)
        IpDns(ip)
        WebsitePort(ip)
        HttpHeaders(website_url)
        CheckSslCertificate(website_url)
        CheckSecurityHeaders(website_url)
        AnalyzeCookies(website_url)
        DetectTechnologies(website_url)
        
        print(f"\n{'='*60}")
        print(f"{Colors.GREEN}Scan completed successfully!{Colors.RESET}")
        print(f"{Colors.YELLOW}Note: This is a basic security scan.{Colors.RESET}")
        print(f"{Colors.YELLOW}For comprehensive testing, use specialized tools.{Colors.RESET}")
        print(f"{'='*60}")
        
        Continue()
        Reset()
        
    except KeyboardInterrupt:
        print(f"\n{BEFORE}{current_time_hour()}{AFTER} {INFO} Scan interrupted by user{red}")
        sys.exit(0)
    except Exception as e:
        Error(e)

if __name__ == "__main__":
    try:
        import socket
        import concurrent.futures
        import requests
        from urllib.parse import urlparse
        import ssl
        import urllib3
        from requests.exceptions import RequestException
        from bs4 import BeautifulSoup
    except ImportError as e:
        print(f"{Colors.RED}Missing module: {e}{Colors.RESET}")
        print(f"{Colors.YELLOW}Install required modules:{Colors.RESET}")
        print("pip install requests beautifulsoup4 urllib3")
        sys.exit(1)
    
    main()
