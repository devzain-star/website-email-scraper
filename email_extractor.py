import re
import requests
from bs4 import BeautifulSoup
import csv
import time

# Updated list of URLs to scrape
urls = [
    "https://www.example.com",
    "https://www.anotherwebsite.com"
]

def extract_emails(page_text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, page_text)
    return emails

def fetch_website_data(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            page_text = soup.get_text()
            emails = extract_emails(page_text)
            if emails:
                return {
                    #"url": url,
                    "emails": ", ".join(emails),
                }
            else:
                return None
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

def save_to_csv(data, filename="scraped_emails.csv"):
    if not data:
        print("No data to save.")
        return

    keys = data[0].keys()
    try:
        with open(filename, mode="w", newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to CSV: {str(e)}")

scraped_data = []
for url in urls:
    print(f"Scraping: {url}")
    data = fetch_website_data(url)
    if data:
        scraped_data.append(data)
    time.sleep(2)

save_to_csv(scraped_data)
