# website-email-scraper
A Python script to scrape emails from websites
# Website Email Scraper

A simple Python script to scrape email addresses from a list of websites.

## Features

- **Email Extraction**: The script fetches websites from a given list and extracts all email addresses.
- **CSV Output**: The emails are saved in a CSV file, with each entry corresponding to a website that contains at least one email address.
- **Error Handling**: If an error occurs while fetching a website, it is ignored, and the script proceeds to the next URL.

## Usage

1. **Clone this repository**:

   ```bash
   git clone https://github.com/your-username/website-email-scraper.git

2. **Install dependencies:**
   Install the required libraries using pip:
    ```bash
   pip install requests beautifulsoup4

4. **Run the script:**
   Execute the script in your terminal/command prompt:
    ```bash
   pip install requests beautifulsoup4

## Example Output

Below is a sample output of the `email_extractor.py` script:

| Website URL                     | Email Address           |
|---------------------------------|-------------------------|
| https://www.example.com         | contact@example.com     |
| https://www.testsite.com        | info@testsite.com       |
| https://www.anotherwebsite.com  | support@another.com     |
