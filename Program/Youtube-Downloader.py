#!/usr/bin/env python3

import yt_dlp
import os
import sys

def download_youtube_video():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    download_path = os.path.join(os.path.dirname(current_dir), "youtube")
    os.makedirs(download_path, exist_ok=True)

    print(f"Download folder: {download_path}")

    link = input("\nYouTube URL: ").strip()

    if not link:
        print("No URL provided!")
        return

    if 'list=' in link:
        if '?list=' in link:
            link = link.split('?list=')[0]
        elif '&list=' in link:
            link = link.split('&list=')[0]

    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'format': 'best[ext=mp4]/best',
        'noplaylist': True,
        'quiet': False,
        'no_warnings': False,
        'ignoreerrors': True,
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'ios'],
                'skip': ['web', 'web_safari', 'web_creator'],
            }
        },
    }

    try:
        print(f"\nStarting MP4 download...")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(link, download=False)
                print(f"\nTitle: {info.get('title', 'Unknown')}")
                print(f"Duration: {info.get('duration', 'Unknown')} seconds")
            except Exception as e:
                print(f"Info fetch error: {e}")

            ydl.download([link])

        print(f"\nDownload successful!")
        print(f"Files saved to: {download_path}")

        files = os.listdir(download_path)
        if files:
            print(f"\nRecent files:")
            for f in files[-5:]:
                fpath = os.path.join(download_path, f)
                size = os.path.getsize(fpath) / (1024*1024)
                print(f"  {f} ({size:.1f} MB)")

    except Exception as e:
        print(f"\nError: {e}")
        print(f"\nTry from command line:")
        print(f"  yt-dlp -f best[ext=mp4] \"{link}\"")
        print("\nUpdate yt-dlp:")
        print("  pip install --upgrade yt-dlp")

    while True:
        print("\n0 - Exit")
        print("1 - Continue")
        choice = input("Choice: ").strip()

        if choice == '0':
            sys.exit(0)
        elif choice == '1':
            download_youtube_video()
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    try:
        download_youtube_video()
    except KeyboardInterrupt:
        print("\nDownload interrupted")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)