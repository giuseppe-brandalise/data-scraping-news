import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup
from tech_news.database import create_news


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
    selector = Selector(text=html_content)

    scraped_data = {}

    scraped_data['url'] = selector.css('link[rel="canonical"]::attr(href)').get()
    scraped_data['title'] = selector.css(".entry-title::text").get().strip()
    scraped_data['timestamp'] = selector.css(".meta-date::text").get()
    scraped_data['writer'] = selector.css("span.author a::text").get()
    reading_time = selector.css("li.meta-reading-time::text").re_first(r"\d+")
    scraped_data['reading_time'] = int(reading_time.split(" ")[0])
    sumary = selector.css("div.entry-content > p:first-of-type *::text").getall()
    scraped_data['summary'] = "".join(sumary).strip()
    scraped_data['category'] = selector.css(".label::text").get()

    return scraped_data


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    url_info = fetch(url)
    data = []
    while len(data) < amount:
        pages = scrape_updates(url_info)
        for page in pages:
            page_data = fetch(page)
            page_info = scrape_news(page_data)
            data.append(page_info)
        url_info = fetch(scrape_next_page_link(url_info))

    news = data[:amount]
    create_news(news)
    return news
