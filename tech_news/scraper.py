import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, timeout=3, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    links = selector.css(".entry-title a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css('a.next.page-numbers::attr(href)').get()
    return next_page


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    scraped_data = {}

    scraped_data['url'] = soup.find(
        "link", {"rel": "canonical"}
    )["href"]
    scraped_data['title'] = soup.find(
        "h1", {"class": "entry-title"}
    ).text.strip()
    scraped_data['timestamp'] = soup.find(
        "li", {"class": "meta-date"}
    ).text
    scraped_data['writer'] = soup.find(
        "h5", {"class": "title-author"}
    ).find("a").text.strip()
    reading_time = soup.find(
        "li", {"class": "meta-reading-time"}
    ).text
    scraped_data['reading_time'] = int(reading_time.split(" ")[0])
    scraped_data['summary'] = soup.find(
        "div", {"class": "entry-content"}
    ).find("p").text.strip()
    scraped_data['category'] = soup.find(
        "span", {"class": "label"}
    ).text

    return scraped_data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
