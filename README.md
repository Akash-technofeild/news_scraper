# BBC News Headlines Scraper 📰

A Python script that scrapes the latest BBC News headlines and saves them into a text file with a timestamp.

## Features
- Fetches headlines from the BBC News website
- Uses **BeautifulSoup** for HTML parsing
- Saves headlines to `headlines.txt` with numbering and date/time
- Fallback mechanism to handle changes in BBC's HTML structure

## Requirements
Make sure you have Python 3 installed, then install the required packages:
```bash
pip install requests beautifulsoup4
Usage
Run the script:

bash
Copy
Edit
python scrape_bbc.py
The script will:

Print the headlines to the terminal

Save them to headlines.txt in the same directory

Example output:

markdown
Copy
Edit
BBC News Headlines - Scraped on 2025-08-15
==================================================

1. UK inflation drops to 2.5%
2. New technology promises greener energy
3. Premier League: Latest match results
...
Notes
This script relies on the current HTML structure of BBC News. If the structure changes, you may need to update the tag/class selectors in the code.

Always respect the site's terms of service and scraping rules.
