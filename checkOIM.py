import requests
import time
from colorama import init, Fore
from datetime import datetime

# Initialize colorama to support ANSI colors in Windows terminals
init()

def check_website_availability(url):
    while True:
        try:
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            
            response = requests.get(url)
            if response.status_code == 200:
                print(Fore.GREEN + f"{current_time} - The website {url} is available.")
                break
            else:
                print(Fore.YELLOW + f"{current_time} - Website {url} not available yet. Status code: {response.status_code}")
        except requests.ConnectionError:
            print(Fore.YELLOW + f"{current_time} - Could not connect to the website {url}")
        
        # Wait for 60 seconds before retrying
        time.sleep(60)

website_url = 'https://via.iom.int/appointment/booking/cavb'

check_website_availability(website_url)
