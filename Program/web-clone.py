import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import mimetypes


def save_webpage(url):
    
    print("\nEnter directory name to save the webpage (or press Enter for 'saved_webpage'):")
    directory_name = input().strip()
    if not directory_name:
        directory_name = "saved_webpage"
    
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        print(f"\nDownloading webpage: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        main_file = os.path.join(directory_name, "index.html")
        with open(main_file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"✓ Main HTML saved as: {main_file}")
        
        resources = []
        
        for link in soup.find_all('link', rel='stylesheet'):
            href = link.get('href')
            if href:
                resources.append(('css', href))
        
        for script in soup.find_all('script', src=True):
            resources.append(('js', script['src']))
        
        for img in soup.find_all('img', src=True):
            resources.append(('img', img['src']))
        
        downloaded_count = 0
        for res_type, res_url in resources:
            try:
                absolute_url = urljoin(url, res_url)
                
                parsed_url = urlparse(absolute_url)
                filename = os.path.basename(parsed_url.path)
                
                if not filename:
                    filename = f"{res_type}_{downloaded_count}"

                if '.' not in filename:
                    content_type, _ = mimetypes.guess_type(absolute_url)
                    if content_type:
                        extension = mimetypes.guess_extension(content_type)
                        if extension:
                            filename += extension
                
                filepath = os.path.join(directory_name, filename)
                
                res_response = requests.get(absolute_url, headers=headers, timeout=5)
                if res_response.status_code == 200:
                    with open(filepath, 'wb') as f:
                        f.write(res_response.content)
                    downloaded_count += 1

                    if res_type == 'css':
                        link['href'] = filename
                    elif res_type == 'js':
                        script['src'] = filename
                    elif res_type == 'img':
                        img['src'] = filename
                        
            except Exception as e:
                print(f"  ✗ Failed to download: {res_url} - {str(e)}")
        
        with open(main_file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        print(f"\n✓ Webpage saved successfully!")
        print(f"✓ Total resources downloaded: {downloaded_count}")
        print(f"✓ Saved in directory: {directory_name}")
        
        print(f"\nDirectory contents:")
        for item in os.listdir(directory_name):
            size = os.path.getsize(os.path.join(directory_name, item))
            print(f"  - {item} ({size} bytes)")
        
    except requests.exceptions.RequestException as e:
        print(f"\n✗ Error downloading the webpage: {str(e)}")
        print("Please check the URL and your internet connection.")
    except Exception as e:
        print(f"\n✗ An unexpected error occurred: {str(e)}")

def main():
    """Főprogram"""
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    print(f"{RED}{BOLD}")
    print("██████╗ ███████╗██████╗  ████████╗██╗ ██████╗ ███████╗██████╗    ██████╗ ██████╗  ██████╗ ")
    print("██╔══██╗██╔════╝██╔══██╗ ╚══██╔══╝██║██╔════╝ ██╔════╝██╔══██╗   ██╔══██╗██╔══██╗██╔═══██╗")
    print("██████╔╝█████╗  ██║  ██║    ██║   ██║██║  ███╗█████╗  ██████╔╝   ██████╔╝██████╔╝██║   ██║")
    print("██╔══██╗██╔══╝  ██║  ██║    ██║   ██║██║   ██║██╔══╝  ██╔══██╗   ██╔═══╝ ██╔══██╗██║   ██║")
    print("██║  ██║███████╗██████╔╝    ██║   ██║╚██████╔╝███████╗██║  ██║   ██║     ██║  ██║╚██████╔╝")
    print("╚═╝  ╚═╝╚══════╝╚═════╝     ╚═╝   ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ")
    print(f"{RESET}")
    
    print("=" * 50)
    print(f"{BOLD}WEBPAGE DOWNLOADER{RESET}")
    print("=" * 50)
    print("\nThis program will download a webpage and all its resources.")
    print("Please enter a valid URL (including http:// or https://)")
    
    while True:
        print("\n" + "-" * 50)
        url = input("\nEnter website URL (or 'quit' to exit): ").strip()
        
        if url.lower() == 'quit':
            print("\nGoodbye!")
            break
        
        if not url.startswith(('http://', 'https://')):
            print("Please include http:// or https:// in the URL")
            continue
        
        save_webpage(url)

        print("\n" + "=" * 50)
        input("Press Enter to download another webpage or close the program...")
        print("=" * 50)

if __name__ == "__main__":
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        print("\nSome required packages are missing. Installing...")
        import subprocess
        import sys
        
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "beautifulsoup4"])
        print("\nPackages installed successfully. Please restart the program.")
        sys.exit(1)
    
    main()