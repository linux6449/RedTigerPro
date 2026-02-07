import requests
from bs4 import BeautifulSoup
import re
import sys

def search_player(riot_id):
    print(f"Searching for information for: {riot_id}")
    if "#" not in riot_id:
        print("Invalid Riot ID format. Please use the format Name#Tag.")
        return

    name, tag = riot_id.split('#')

    # *** IMPORTANT NOTE ***
    # This implementation is based on web-scraping third-party websites.
    # Web-scraping is susceptible to website structure changes and may
    # violate the terms of service of the respective website.
    # The examples used here are hypothetical and for illustration only.
    # A robust solution would ideally use official APIs (if available)
    # or rely on third-party APIs (while respecting their terms).

    # *** Example 1: Hypothetical tracker page for recent matches ***
    tracker_url_matches = f"https://hypothetical-valorant-tracker.de/player/{name}-{tag}/matches"
    print(f"\nAttempting to retrieve recent matches from: {tracker_url_matches}...")
    try:
        response_matches = requests.get(tracker_url_matches)
        response_matches.raise_for_status()
        soup_matches = BeautifulSoup(response_matches.content, 'html.parser')

        match_summaries = soup_matches.find_all("div", class_="match-summary-item")
        if match_summaries:
            print("\nRecently played matches (possibly):")
            for i, match in enumerate(match_summaries[:5]):
                print(f"- Match {i+1}: {match.get_text(separator=' ', strip=True)[:80]}...")
        else:
            print("No match information found on this page.")

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving the match page: {e}")
    except Exception as e:
        print(f"Error processing match data: {e}")

    # *** Example 2: Hypothetical tracker page for general statistics ***
    tracker_url_stats = f"https://hypothetical-valorant-tracker.de/player/{name}-{tag}/stats"
    print(f"\nAttempting to retrieve general statistics from: {tracker_url_stats}...")
    try:
        response_stats = requests.get(tracker_url_stats)
        response_stats.raise_for_status()
        soup_stats = BeautifulSoup(response_stats.content, 'html.parser')

        winrate_element = soup_stats.find("div", class_="winrate")
        if winrate_element:
            winrate = winrate_element.get_text(strip=True)
            print(f"  - Winrate (possibly): {winrate}")

        most_played_agent_element = soup_stats.find("div", class_="most-played-agent")
        if most_played_agent_element:
            most_played_agent = most_played_agent_element.get_text(strip=True)
            print(f"  - Most played agent (possibly): {most_played_agent}")

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving the statistics page: {e}")
    except Exception as e:
        print(f"Error processing statistics data: {e}")

    # *** Example 3: Simple social media search (rudimentary) ***
    print("\nSearching social media (manual verification recommended):")
    social_platforms = ["Twitter", "Twitch", "YouTube"]
    for platform in social_platforms:
        search_query = f"Valorant {name} #{tag} {platform}"
        search_url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
        print(f"- Search on {platform}: {search_url}")
        print("  (Results must be verified manually)")
    
    print("\nPress Enter to continue...")
    input()

if __name__ == "__main__":
    riot_id_input = input("Enter the Valorant Riot ID (Name#Tag): ")
    search_player(riot_id_input)
    print("\nPress Enter to exit...")
    input()
