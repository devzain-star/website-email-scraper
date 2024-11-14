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

# Function to extract emails from the website's content
def extract_emails(page_text):
    # Regular expression to find email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, page_text)
    return emails

# Function to fetch website data with proper error handling
def fetch_website_data(url):
    try:
        response = requests.get(url, timeout=10)  # Added timeout
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            # Get the text content of the page to search for emails
            page_text = soup.get_text()
            emails = extract_emails(page_text)
            if emails:
                return {
                    #"url": url,
                    "emails": ", ".join(emails),  # Join emails if there are multiple
                }
            else:
                return None  # Return None if no emails are found
        else:
            return None  # Return None if status code is not 200
    except requests.exceptions.RequestException as e:
        return None  # Return None if an error occurs while making the request

# Function to save data in CSV format
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

# Scrape data from all URLs with a delay to avoid rate-limiting
scraped_data = []
for url in urls:
    print(f"Scraping: {url}")
    data = fetch_website_data(url)
    if data:  # Only add data if emails were found
        scraped_data.append(data)
    time.sleep(2)  # Sleep for 2 seconds between requests to avoid rate-limiting

# Save the data to CSV
save_to_csv(scraped_data)
