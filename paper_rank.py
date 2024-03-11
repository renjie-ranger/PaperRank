from datetime import datetime
import requests
from bs4 import BeautifulSoup
import argparse


def fetch_recent_dates_from_arxiv(field):
    # Target URL
    url = f"https://arxiv.org/list/cs.{field}/recent"
    
    # Send HTTP GET request to fetch webpage content
    response = requests.get(url)
    
    # Parse webpage content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all <li> elements containing dates
    dates_list = soup.find_all('li')
    recent_dates = []
    for date in dates_list:
        date_text = date.get_text(strip=True)
        if date_text and date_text not in recent_dates:  # Avoid duplicates
            recent_dates.append(date_text)
            if len(recent_dates) == 5:  # Only need the first five unique dates
                break

    # Convert date text to datetime objects for later use
    recent_dates = [datetime.strptime(date, '%a, %d %b %Y') for date in recent_dates[:5]]
    return recent_dates


def build_urls(dates, field):
    base_url = f"https://papers.cool/arxiv/cs.{field}?date="
    urls = [base_url + date.strftime('%Y-%m-%d') + "&show=200" for date in dates]
    return urls


def fetch_and_sort_papers(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    papers_info = []

    for paper in soup.find_all('div', class_='panel paper'):
        title = paper.find('a', class_='title-link').text.strip()
        pdf_opens_text = paper.find('a', class_='title-pdf').find('sup').text.strip()
        kimi_opens_text = paper.find('a', class_='title-kimi').find('sup').text.strip()
        pdf_opens = int(pdf_opens_text) if pdf_opens_text.isdigit() else 0
        kimi_opens = int(kimi_opens_text) if kimi_opens_text.isdigit() else 0
        total_opens = pdf_opens + kimi_opens
        papers_info.append((title, total_opens))

    sorted_papers = sorted(papers_info, key=lambda x: x[1], reverse=True)
    return sorted_papers[:10]


def main(field):
    # Use the new function to fetch dates
    recent_dates = fetch_recent_dates_from_arxiv(field)
    urls = build_urls(recent_dates, field)

    for i, url in enumerate(urls):
        print(f"Date: {recent_dates[i].strftime('%Y-%m-%d')}, URL: {url}")
        top_papers = fetch_and_sort_papers(url)
        print("Top 10 Papers:")
        for title, num in top_papers:
            print(num, title)
        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Choose the field you want to rank the papers, currently support CL, LG, AI, CV on Arxiv")
    parser.add_argument("-f", "--field", type=str, help="Only input one element from the list ['CL','LG','AI','CV']", default="CL")

    # Parse command line arguments
    args = parser.parse_args()
    main(args.field)