import re
import requests
import os
import time
from pathlib import Path

def get_tiktok_folder():
    """Finds the tiktok folder"""
    current_dir = Path(__file__).parent.absolute()
    parent_dir = current_dir.parent
    tiktok_folder = parent_dir / "tiktok"
    
    if not tiktok_folder.exists():
        tiktok_folder.mkdir(exist_ok=True)
    
    return str(tiktok_folder)

def download_tiktok_video(url):
    """Downloads TikTok video"""
    try:
        api_url = f"https://tikwm.com/api?url={url}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json',
        }
        
        print("Getting video information...")
        response = requests.get(api_url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('code') == 0 and 'data' in data:
                video_url = data['data'].get('play')
                
                if video_url:
                    print(f"Downloading video: {video_url}")
                    
                    download_folder = get_tiktok_folder()
                    
                    timestamp = int(time.time())
                    filename = f"tiktok_video_{timestamp}.mp4"
                    output_path = os.path.join(download_folder, filename)
                    
                    video_response = requests.get(video_url, stream=True, headers=headers)
                    
                    if video_response.status_code == 200:
                        with open(output_path, 'wb') as f:
                            for chunk in video_response.iter_content(chunk_size=8192):
                                if chunk:
                                    f.write(chunk)
                        
                        file_size = os.path.getsize(output_path) / (1024 * 1024)
                        print(f"✅ Successful download: {output_path} ({file_size:.2f} MB)")
                        print(f"Full path: {os.path.abspath(output_path)}")
                        
                        return output_path
                    else:
                        print("❌ Failed to download the video")
                else:
                    print("❌ Video URL not found")
            else:
                print("❌ Error in API response")
        else:
            print(f"❌ API error: {response.status_code}")
            
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
    
    return None

def main():
    print("=" * 50)
    print("TikTok Video Downloader")
    print("=" * 50)
    
    url = input("Please enter the TikTok video link: ").strip()
    
    if not url:
        print("❌ No URL provided")
        return
    
    print(f"\nProcessing: {url}")
    downloaded_file = download_tiktok_video(url)
    
    if downloaded_file:
        print("\n🎉 Video successfully downloaded!")
    else:
        print("\n⚠️ Download failed.")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    try:
        import requests
    except ImportError:
        print("❌ The 'requests' library is not installed!")
        print("Install it with: pip install requests")
        exit(1)
    
    main()