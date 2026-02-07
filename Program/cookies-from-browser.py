import sqlite3
import os
import sys
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import platform

class BrowserCookieManager:
    
    def __init__(self):
        self.system = platform.system().lower()
        self.user_home = str(Path.home())
        self.browsers = self._detect_browsers()
        
    def _detect_browsers(self) -> Dict:
        browsers = {}
        
        chrome_based = {
            'google-chrome': {
                'name': 'Google Chrome',
                'paths': self._get_chrome_paths('google-chrome'),
                'icon': '🟡'
            },
            'chromium': {
                'name': 'Chromium',
                'paths': self._get_chrome_paths('chromium'),
                'icon': '🔵'
            },
            'brave': {
                'name': 'Brave Browser',
                'paths': self._get_chrome_paths('brave-browser'),
                'icon': '🦁'
            },
            'microsoft-edge': {
                'name': 'Microsoft Edge',
                'paths': self._get_chrome_paths('microsoft-edge'),
                'icon': '🌀'
            },
            'vivaldi': {
                'name': 'Vivaldi',
                'paths': self._get_chrome_paths('vivaldi'),
                'icon': '🔴'
            },
            'opera': {
                'name': 'Opera',
                'paths': self._get_opera_paths(),
                'icon': '🔴'
            },
            'opera-gx': {
                'name': 'Opera GX',
                'paths': self._get_opera_gx_paths(),
                'icon': '🎮'
            }
        }
        
        firefox_based = {
            'firefox': {
                'name': 'Mozilla Firefox',
                'paths': self._get_firefox_paths(),
                'icon': '🦊'
            },
            'librewolf': {
                'name': 'LibreWolf',
                'paths': self._get_librewolf_paths(),
                'icon': '🐺'
            }
        }
        
        all_browsers = {**chrome_based, **firefox_based}
        
        for browser_id, browser_info in all_browsers.items():
            for path in browser_info['paths']:
                if path and os.path.exists(path):
                    browsers[browser_id] = browser_info
                    break
        
        return browsers
    
    def _get_chrome_paths(self, browser_name: str) -> List[str]:
        paths = []
        
        if self.system == 'linux':
            base_paths = [
                f'{self.user_home}/.config/{browser_name}',
                f'{self.user_home}/.config/{browser_name}-stable',
                f'{self.user_home}/snap/{browser_name}/current/.config/{browser_name}',
                f'{self.user_home}/.var/app/com.{browser_name}.{browser_name}/config/{browser_name}'
            ]
            
        elif self.system == 'darwin':
            base_paths = [
                f'{self.user_home}/Library/Application Support/{browser_name}',
                f'{self.user_home}/Library/Application Support/{browser_name.capitalize()}'
            ]
            
        else:
            appdata = os.getenv('APPDATA', '')
            local_appdata = os.getenv('LOCALAPPDATA', '')
            base_paths = [
                f'{local_appdata}/{browser_name}/User Data',
                f'{appdata}/{browser_name}/User Data'
            ]
        
        for base in base_paths:
            paths.append(os.path.join(base, 'Default'))
            paths.append(os.path.join(base, 'Profile 1'))
        
        return paths
    
    def _get_opera_paths(self) -> List[str]:
        paths = []
        
        if self.system == 'linux':
            paths = [
                f'{self.user_home}/.config/opera',
                f'{self.user_home}/snap/opera/current/.config/opera'
            ]
        elif self.system == 'darwin':
            paths = [f'{self.user_home}/Library/Application Support/com.operasoftware.Opera']
        else:
            appdata = os.getenv('APPDATA', '')
            paths = [f'{appdata}/Opera Software/Opera Stable']
        
        return paths
    
    def _get_opera_gx_paths(self) -> List[str]:
        paths = []
        
        if self.system == 'linux':
            paths = [f'{self.user_home}/.config/opera-gx']
        elif self.system == 'darwin':
            paths = [f'{self.user_home}/Library/Application Support/com.operasoftware.OperaGX']
        else:
            appdata = os.getenv('APPDATA', '')
            paths = [f'{appdata}/Opera Software/Opera GX Stable']
        
        return paths
    
    def _get_firefox_paths(self) -> List[str]:
        paths = []
        
        if self.system == 'linux':
            paths = [
                f'{self.user_home}/.mozilla/firefox',
                f'{self.user_home}/snap/firefox/common/.mozilla/firefox'
            ]
        elif self.system == 'darwin':
            paths = [f'{self.user_home}/Library/Application Support/Firefox/Profiles']
        else:
            appdata = os.getenv('APPDATA', '')
            paths = [f'{appdata}/Mozilla/Firefox/Profiles']
        
        return paths
    
    def _get_librewolf_paths(self) -> List[str]:
        paths = []
        
        if self.system == 'linux':
            paths = [
                f'{self.user_home}/.librewolf',
                f'{self.user_home}/.var/app/io.gitlab.librewolf-community/.librewwolf'
            ]
        
        return paths
    
    def find_cookie_files(self, browser_id: str) -> List[Tuple[str, str]]:
        cookie_files = []
        browser_info = self.browsers.get(browser_id)
        
        if not browser_info:
            return cookie_files
        
        for profile_path in browser_info['paths']:
            if not profile_path or not os.path.exists(profile_path):
                continue
            
            if browser_id in ['google-chrome', 'chromium', 'brave', 'microsoft-edge', 
                            'vivaldi', 'opera', 'opera-gx']:
                cookie_file = os.path.join(profile_path, 'Cookies')
                if os.path.exists(cookie_file):
                    cookie_files.append((profile_path, cookie_file))
            
            elif browser_id in ['firefox', 'librewolf']:
                try:
                    for item in os.listdir(profile_path):
                        item_path = os.path.join(profile_path, item)
                        if os.path.isdir(item_path):
                            cookie_file = os.path.join(item_path, 'cookies.sqlite')
                            if os.path.exists(cookie_file):
                                cookie_files.append((item_path, cookie_file))
                except (FileNotFoundError, PermissionError):
                    continue
        
        return cookie_files
    
    def read_chrome_cookies(self, cookie_file: str) -> List[Dict]:
        cookies = []
        
        try:
            temp_file = f"{cookie_file}.temp"
            shutil.copy2(cookie_file, temp_file)
            
            conn = sqlite3.connect(temp_file)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT host_key, name, value, path, expires_utc, 
                       is_secure, is_httponly, has_expires
                FROM cookies
                ORDER BY host_key, name
            """)
            
            for row in cursor.fetchall():
                cookie = {
                    'domain': row[0],
                    'name': row[1],
                    'value': row[2],
                    'path': row[3],
                    'expires': row[4],
                    'secure': bool(row[5]),
                    'httponly': bool(row[6]),
                    'has_expires': bool(row[7]),
                    'type': 'chrome'
                }
                cookies.append(cookie)
            
            conn.close()
            os.remove(temp_file)
            
        except Exception as e:
            print(f"  [!] Chrome cookie read error: {e}")
        
        return cookies
    
    def read_firefox_cookies(self, cookie_file: str) -> List[Dict]:
        cookies = []
        
        try:
            conn = sqlite3.connect(f"file:{cookie_file}?mode=ro", uri=True)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT host, name, value, path, expiry, 
                       isSecure, isHttpOnly
                FROM moz_cookies
                ORDER BY host, name
            """)
            
            for row in cursor.fetchall():
                cookie = {
                    'domain': row[0],
                    'name': row[1],
                    'value': row[2],
                    'path': row[3],
                    'expires': row[4],
                    'secure': bool(row[5]),
                    'httponly': bool(row[6]),
                    'type': 'firefox'
                }
                cookies.append(cookie)
            
            conn.close()
            
        except Exception as e:
            print(f"  [!] Firefox cookie read error: {e}")
        
        return cookies
    
    def display_cookies_table(self, browser_id: str):
        if browser_id not in self.browsers:
            print(f"\n[!] Unknown browser: {browser_id}")
            return
        
        browser_info = self.browsers[browser_id]
        cookie_files = self.find_cookie_files(browser_id)
        
        if not cookie_files:
            print(f"\n{browser_info['icon']} {browser_info['name']} - No cookie files found")
            return
        
        total_cookies = 0
        
        for profile_path, cookie_file in cookie_files:
            print(f"\n{'='*80}")
            print(f"{browser_info['icon']} {browser_info['name']}")
            print(f"{'='*80}")
            print(f"Profile: {os.path.basename(profile_path)}")
            print(f"File: {cookie_file}")
            print(f"{'-'*80}")
            
            if browser_id in ['firefox', 'librewolf']:
                cookies = self.read_firefox_cookies(cookie_file)
            else:
                cookies = self.read_chrome_cookies(cookie_file)
            
            if not cookies:
                print("  No cookies in this profile")
                continue
            
            domains = {}
            for cookie in cookies:
                domain = cookie['domain']
                if domain not in domains:
                    domains[domain] = []
                domains[domain].append(cookie)
            
            sorted_domains = sorted(domains.keys())
            
            domain_count = 0
            for domain in sorted_domains:
                domain_cookies = domains[domain]
                domain_count += 1
                
                print(f"\n  📌 {domain} ({len(domain_cookies)} cookies)")
                print(f"  {'─' * (len(domain) + 15)}")
                
                cookie_count = 0
                for cookie in domain_cookies:
                    cookie_count += 1
                    total_cookies += 1
                    
                    flags = []
                    if cookie.get('secure', False):
                        flags.append("🔒")
                    if cookie.get('httponly', False):
                        flags.append("🌐")
                    
                    flags_str = ' '.join(flags)
                    
                    value = cookie['value']
                    if len(value) > 40:
                        value = value[:37] + "..."
                    
                    print(f"    {cookie_count:3d}. {cookie['name']}")
                    print(f"        Value: {value} {flags_str}")
                    print(f"        Path: {cookie['path']}")
                    
                    expires = cookie.get('expires', 0)
                    if expires and expires > 10000000000:
                        expires = expires // 1000000
                    
                    if expires == 0:
                        expires_str = "Session"
                    elif expires < 1000000000:
                        expires_str = datetime.fromtimestamp(expires).strftime("%Y-%m-%d %H:%M")
                    else:
                        expires_str = "Unknown format"
                    
                    print(f"        Expires: {expires_str}")
                    print()
                
                if len(domain_cookies) > 10:
                    print(f"    ... {len(domain_cookies) - 10} more cookies")
            
            print(f"\n  Total: {len(cookies)} cookies in this profile")
        
        return total_cookies
    
    def display_summary(self):
        print("\n" + "="*80)
        print("🎯 BROWSER COOKIE MANAGER")
        print("="*80)
        print(f"System: {platform.system()} {platform.release()}")
        print(f"User: {os.getenv('USER', 'Unknown')}")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80)
        
        if not self.browsers:
            print("\n[!] No browsers detected!")
            print("    Check installations or paths.")
            return
        
        print(f"\n📊 Available browsers ({len(self.browsers)}):")
        print("-" * 40)
        
        browser_list = []
        for browser_id, browser_info in self.browsers.items():
            cookie_files = self.find_cookie_files(browser_id)
            profile_count = len(cookie_files)
            browser_list.append((browser_info['icon'], browser_info['name'], profile_count))
        
        browser_list.sort(key=lambda x: x[1])
        
        for icon, name, profile_count in browser_list:
            profile_text = f"({profile_count} profiles)" if profile_count > 0 else "(no profiles)"
            print(f"  {icon} {name:20} {profile_text}")
        
        print("\nℹ️  Usage: Enter browser number (e.g., '1'), or 'all' for all browsers")
        print("   'exit' to quit, Enter to continue")
        print("="*80)
        
        return browser_list
    
    def display_all_cookies(self):
        total_all_cookies = 0
        
        print("\n" + "="*80)
        print("🌐 ALL BROWSER COOKIES")
        print("="*80)
        
        for browser_id in sorted(self.browsers.keys()):
            browser_info = self.browsers[browser_id]
            print(f"\n{'━' * 80}")
            print(f"{browser_info['icon']} {browser_info['name'].upper()}")
            print(f"{'━' * 80}")
            
            total_cookies = self.display_cookies_table(browser_id)
            total_all_cookies += total_cookies
        
        print(f"\n{'='*80}")
        print(f"📈 TOTAL: {total_all_cookies} cookies from {len(self.browsers)} browsers")
        print("="*80)
        
        return total_all_cookies

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    manager = BrowserCookieManager()
    
    while True:
        clear_screen()
        browser_list = manager.display_summary()
        
        if not browser_list:
            print("\n[!] No browsers in list")
            print("\n⏎  Press Enter to exit...")
            input()
            break
        
        print("\n🎯 SELECTION:")
        print("-" * 40)
        
        for i, (icon, name, profile_count) in enumerate(browser_list, 1):
            print(f"  [{i:2}] {icon} {name}")
        
        print(f"  [ A ] All browsers")
        print(f"  [ X ] Exit")
        print("-" * 40)
        
        choice = input("\n👉 Choose (number/A/X/Enter=exit): ").strip().lower()
        
        if choice == '':
            print("\n👋 Goodbye!")
            break
        elif choice == 'x' or choice == 'exit':
            print("\n👋 Goodbye!")
            break
        elif choice == 'a' or choice == 'all':
            clear_screen()
            manager.display_all_cookies()
            print("\n⏎  Back to main menu...")
            input()
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(browser_list):
                browser_id = list(manager.browsers.keys())[index]
                clear_screen()
                manager.display_cookies_table(browser_id)
                print("\n⏎  Back to main menu...")
                input()
            else:
                print(f"\n[!] Invalid number: {choice}")
                print("\n⏎  Try again...")
                input()
        else:
            print(f"\n[!] Invalid choice: {choice}")
            print("\n⏎  Try again...")
            input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Program interrupted")
        print("👋 Goodbye!")
    except Exception as e:
        print(f"\n[!] Unexpected error: {e}")
        print("\n⏎  Press Enter to exit...")
        input()