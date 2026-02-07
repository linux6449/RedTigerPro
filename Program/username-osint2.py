import requests
import sys
import time
from urllib.parse import quote

def print_banner():
    banner = r"""
 ‚ĖĄ‚Ėą    ‚Ėą‚ĖĄ     ‚ĖĄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą ‚Ėą‚Ėą‚Ėą‚ĖĄ‚ĖĄ‚ĖĄ‚ĖĄ       ‚Ėą‚Ėą‚Ėą      ‚ĖĄ‚Ėą  ‚ĖÄ‚Ėą‚Ėą‚Ėą‚Ėą    ‚Ėź‚Ėą‚Ėą‚Ėą‚Ėą‚ĖÄ     ‚Ėą‚Ėą‚Ėą              ‚Ėą‚Ėą‚Ėą        ‚ĖĄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą    ‚ĖĄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą  ‚ĖĄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą    ‚ĖĄ‚Ėą   ‚ĖĄ‚Ėą‚ĖĄ    ‚ĖĄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą    ‚ĖĄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą 
‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą ‚Ėą‚Ėą‚Ėą‚ĖÄ‚ĖÄ‚ĖÄ‚Ėą‚Ėą‚ĖĄ ‚ĖÄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ĖĄ ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą‚ĖĆ   ‚Ėą‚Ėą‚Ėą‚Ėą‚ĖÄ  ‚ĖÄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ĖĄ      ‚ĖÄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ĖĄ   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą ‚ĖĄ‚Ėą‚Ėą‚Ėą‚ĖÄ   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą 
‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą    ‚ĖÄ‚Ėą‚Ėą‚Ėą‚ĖÄ‚ĖÄ‚Ėą‚Ėą ‚Ėą‚Ėą‚Ėą‚ĖĆ    ‚Ėą‚Ėą‚Ėą  ‚Ėź‚Ėą‚Ėą‚Ėą       ‚ĖÄ‚Ėą‚Ėą‚Ėą‚ĖÄ‚ĖÄ‚Ėą‚Ėą         ‚ĖÄ‚Ėą‚Ėą‚Ėą‚ĖÄ‚ĖÄ‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą ‚Ėą‚Ėą‚Ėą    ‚Ėą‚ĖÄ    ‚Ėą‚Ėą‚Ėą‚Ėź‚Ėą‚Ėą‚ĖÄ     ‚Ėą‚Ėą‚Ėą    ‚Ėą‚ĖÄ    ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą 
‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą     ‚Ėą‚Ėą‚Ėą   ‚ĖÄ ‚Ėą‚Ėą‚Ėą‚ĖĆ    ‚ĖÄ‚Ėą‚Ėą‚Ėą‚ĖĄ‚Ėą‚Ėą‚Ėą‚ĖÄ        ‚Ėą‚Ėą‚Ėą   ‚ĖÄ          ‚Ėą‚Ėą‚Ėą   ‚ĖÄ  ‚ĖĄ‚Ėą‚Ėą‚Ėą‚ĖĄ‚ĖĄ‚ĖĄ‚ĖĄ‚Ėą‚Ėą‚ĖÄ   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą ‚Ėą‚Ėą‚Ėą         ‚ĖĄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ĖÄ     ‚ĖĄ‚Ėą‚Ėą‚Ėą‚ĖĄ‚ĖĄ‚ĖĄ      ‚ĖĄ‚Ėą‚Ėą‚Ėą‚ĖĄ‚ĖĄ‚ĖĄ‚ĖĄ‚Ėą‚Ėą‚ĖÄ 
‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą ‚ĖÄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą     ‚Ėą‚Ėą‚Ėą     ‚Ėą‚Ėą‚Ėą‚ĖĆ    ‚Ėą‚Ėą‚Ėą‚Ėą‚ĖÄ‚Ėą‚Ėą‚ĖĄ         ‚Ėą‚Ėą‚Ėą              ‚Ėą‚Ėą‚Ėą     ‚ĖÄ‚ĖÄ‚Ėą‚Ėą‚Ėą‚ĖÄ‚ĖÄ‚ĖÄ‚ĖÄ‚ĖÄ   ‚ĖÄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą ‚Ėą‚Ėą‚Ėą        ‚ĖÄ‚ĖÄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ĖĄ    ‚ĖÄ‚ĖÄ‚Ėą‚Ėą‚Ėą‚ĖÄ‚ĖÄ‚ĖÄ     ‚ĖÄ‚ĖÄ‚Ėą‚Ėą‚Ėą‚ĖÄ‚ĖÄ‚ĖÄ‚ĖÄ‚ĖÄ   
‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą     ‚Ėą‚Ėą‚Ėą     ‚Ėą‚Ėą‚Ėą    ‚Ėź‚Ėą‚Ėą‚Ėą  ‚ĖÄ‚Ėą‚Ėą‚Ėą        ‚Ėą‚Ėą‚Ėą              ‚Ėą‚Ėą‚Ėą     ‚ĖÄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą ‚Ėą‚Ėą‚Ėą    ‚Ėą‚ĖĄ    ‚Ėą‚Ėą‚Ėą‚Ėź‚Ėą‚Ėą‚ĖĄ     ‚Ėą‚Ėą‚Ėą    ‚Ėą‚ĖĄ  ‚ĖÄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą 
‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą     ‚Ėą‚Ėą‚Ėą     ‚Ėą‚Ėą‚Ėą   ‚ĖĄ‚Ėą‚Ėą‚Ėą     ‚Ėą‚Ėą‚Ėą‚ĖĄ      ‚Ėą‚Ėą‚Ėą              ‚Ėą‚Ėą‚Ėą       ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą ‚ĖÄ‚Ėą‚Ėą‚Ėą‚ĖĄ   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą 
 ‚ĖÄ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ĖÄ    ‚Ėą‚Ėą‚Ėą    ‚Ėą‚ĖÄ   ‚ĖÄ‚Ėą   ‚Ėą‚ĖÄ     ‚ĖĄ‚Ėą‚Ėą‚Ėą‚Ėą‚ĖÄ   ‚Ėą‚ĖÄ   ‚Ėą‚Ėą‚Ėą‚Ėą       ‚Ėą‚Ėą‚Ėą‚ĖĄ    ‚ĖĄ‚Ėą‚Ėą‚Ėą‚Ėą‚ĖÄ           ‚ĖĄ‚Ėą‚Ėą‚Ėą‚Ėą‚ĖÄ     ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚ĖÄ  ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ĖÄ    ‚Ėą‚Ėą‚Ėą   ‚ĖÄ‚Ėą‚ĖÄ   ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą   ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą 
                                                                                                  ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą                           ‚ĖÄ                        ‚Ėą‚Ėą‚Ėą    ‚Ėą‚Ėą‚Ėą 
    """
    print("\033[91m" + banner + "\033[0m")
    print("\033[93m" + "="*60 + "\033[0m")
    print("\033[93m" + "Find every social media account with BlueTiger!" + "\033[0m")
    print("\033[93m" + "="*60 + "\033[0m")
    time.sleep(1)

def check_username(username):
    platforms = {
        # Social Media
        "Instagram": f"https://www.instagram.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Twitter/X": f"https://twitter.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Pinterest": f"https://pinterest.com/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "VK": f"https://vk.com/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "Discord": f"https://discord.com/users/{username}",
        
        # Gaming
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Epic Games": f"https://www.epicgames.com/account/personal?productName={username}",
        "Roblox": f"https://www.roblox.com/user.aspx?username={username}",
        "Origin/EA": f"https://www.ea.com/de-de/search?q={username}",
        "Ubisoft": f"https://www.ubisoft.com/de-de/search?q={username}",
        "Battle.net": f"https://blizzard.com/search?q={username}",
        "League of Legends": f"https://www.op.gg/summoners/euw/{username}",
        "Valorant": f"https://tracker.gg/valorant/profile/riot/{username}",
        
        # Anime & Manga
        "AniWorld.to": f"https://aniworld.to/user/{quote(username)}/profile",
        "MyAnimeList": f"https://myanimelist.net/profile/{username}",
        "AniList": f"https://anilist.co/user/{username}",
        "Crunchyroll": f"https://www.crunchyroll.com/user/{username}",
        
        # Other Platforms
        "Guns.lol": f"https://guns.lol/{username}",
        "Fandom": f"https://community.fandom.com/wiki/User:{username}",
        "DeviantArt": f"https://{username}.deviantart.com",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Kick": f"https://kick.com/{username}",
        "Telegram": f"https://t.me/{username}",
        "Rumble": f"https://rumble.com/user/{username}",
        "9GAG": f"https://9gag.com/u/{username}",
        "Quora": f"https://www.quora.com/profile/{username}",
        "Wattpad": f"https://www.wattpad.com/user/{username}",
        "Letterboxd": f"https://letterboxd.com/{username}",
        "Gaia Online": f"https://www.gaiaonline.com/profiles/{username}",
        "IMVU": f"https://www.imvu.com/next/#/users/{username}",
    }

    print(f"\n\033[94m[!] Hunting '{username}' in the dark corners of the internet...\n\033[0m")

    found_count = 0
    
    for platform, url in platforms.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"\033[92m[✓] {platform}: FOUND! -> {url}\033[0m")
                found_count += 1
            else:
                print(f"\033[91m[✗] {platform}: Not found or private.\033[0m")
        except requests.RequestException:
            print(f"\033[93m[⚠] {platform}: Error (site blocked us or is down)\033[0m")
    
    print(f"\n\033[94m[!] Scan completed! Found {found_count} potential profiles.\033[0m")

if __name__ == "__main__":
    print_banner()
    target = input("\n\033[96mEnter target username: \033[0m")
    check_username(target)
    
    # Új sor: Enter lenyomására várás bezárás előtt
    input("\n\033[96mPress Enter to close...\033[0m")