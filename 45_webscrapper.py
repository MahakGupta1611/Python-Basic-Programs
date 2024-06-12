import requests
from bs4 import BeautifulSoup

# Function to fetch and parse HTML content
def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

# Function to extract article titles
def extract_titles(soup):
    titles = []
    # Assuming article titles are in <h2> tags with a class 'title'
    for title_tag in soup.find_all('h2', class_='title'):
        titles.append(title_tag.get_text())
    return titles

# Main function to scrape the website
def main():
    url = 'https://example-news-website.com'  # Replace with the target website URL
    soup = fetch_html(url)
    
    if soup:
        titles = extract_titles(soup)
        print("Article Titles:")
        for idx, title in enumerate(titles, start=1):
            print(f"{idx}. {title}")

if __name__ == "__main__":
    main()

