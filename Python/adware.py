import webbrowser
import time

def open_ad_website():
    website_url = 'https://www.example.com'  # Specify the URL of the website to open

    while True:
        webbrowser.open(website_url)
        time.sleep(1)  # Adjust the delay as desired

open_ad_website()
