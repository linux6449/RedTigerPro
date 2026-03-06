import yt_dlp
import os
import sys

def download_instagram_video():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    download_path = os.path.join(os.path.dirname(current_dir), "instagram")
    os.makedirs(download_path, exist_ok=True)

    print(f"Download folder: {download_path}")

    link = input("\nInstagram video URL: ").strip()

    if not link:
        print("No URL provided!")
        return

    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'format': 'best',
        'quiet': False,
    }

    try:
        print(f"\nStarting video download...")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        print(f"\nDownload successful!")
        print(f"Location: {download_path}")

        files = os.listdir(download_path)
        if files:
            latest_file = max([os.path.join(download_path, f) for f in files], key=os.path.getctime)
            filename = os.path.basename(latest_file)
            size = os.path.getsize(latest_file) / (1024*1024)
            print(f"Downloaded file: {filename} ({size:.1f} MB)")

    except Exception as e:
        print(f"\nError: {e}")

    while True:
        print("\n0 - Exit")
        print("1 - New download")
        choice = input("Choice: ").strip()

        if choice == '0':
            sys.exit(0)
        elif choice == '1':
            download_instagram_video()
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    try:
        print("=== Instagram Video Downloader ===\n")
        download_instagram_video()
    except KeyboardInterrupt:
        print("\nDownload interrupted")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)