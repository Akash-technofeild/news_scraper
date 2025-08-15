import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.bbc.com/news"
response = requests.get(url)
print("Status code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

# Try targeting BBC's specific headline class
headlines = soup.find_all("h3", class_="gs-c-promo-heading__title")

# Fallback to generic h2 if no targeted hits
if not headlines:
    headlines = soup.find_all("h2")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Found {len(headlines)} headlines.")

with open("headlines.txt", "w", encoding="utf-8") as file:
    file.write(f"BBC News Headlines - Scraped on {timestamp}\n")
    file.write("=" * 50 + "\n\n")
    
    for i, h in enumerate(headlines, start=1):
        text = h.get_text(strip=True)
        print(f"{i}. {text}")
        file.write(f"{i}. {text}\n")

print("\nHeadlines saved to headlines.txt")
