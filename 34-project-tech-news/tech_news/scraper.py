import requests
import time
from parsel import Selector

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        for _ in range(5):
            time.sleep(1)
            response = requests.get(url, timeout=3)
            response.raise_for_status()
    except requests.Timeout:
        return None
    except requests.HTTPError:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urls = selector.css(".tec--card__info h3 a::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css(".tec--btn::attr(href)").get()
    return next_page_url


# funções auxiliar ao requisito 04:
def test_writer(html_content):
    selector = Selector(text=html_content)
    writer = (
        selector.css("div.tec--author__info p:first-child a::text").get()
        or selector.css(".tec--timestamp__item a::text").get()
        or selector.css(".z--m-none.z--truncate.z--font-bold::text").get()
    )
    if writer:
        writer = writer.strip()
    return writer


def test_comments_count(html_content):
    selector = Selector(text=html_content)
    # comments_count = selector.css("#js-comments-btn::text").get()
    # if comments_count is None:
    #     comments_count = 0
    # else:
    #     comments_count = int(comments_count.strip(" Comentários"))
    comments_count = int(
        selector.css("button.tec--btn::text").getall()[1].split(" ")[1]
    )
    return comments_count


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("head link[rel= 'canonical']::attr(href)").get()
    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count is None:
        shares_count = 0
    else:
        shares_count = int(shares_count.strip(" Compartilharam"))
    summary = ""
    for characters in selector.css(
        "div.tec--article__body > p:first-child *::text"
    ).getall():
        summary += characters
    sources = []
    for source in selector.css("div.z--mb-16 div a::text").getall():
        sources.append(source.strip())
    categories = []
    for category in selector.css("#js-categories a::text").getall():
        categories.append(category.strip())
    specific_news = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": test_writer(html_content),
        "shares_count": shares_count,
        "comments_count": test_comments_count(html_content),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }
    return specific_news


# Requisito 5
def get_tech_news(amount):
    URL_BASE = "https://www.tecmundo.com.br/novidades"
    html = fetch(URL_BASE)
    news = scrape_novidades(html)
    while len(news) < amount:
        next_page = scrape_next_page_link(html)
        html = fetch(next_page)
        news.extend(scrape_novidades(html))

    news = news[:amount]

    data = []
    for url in news:
        result = fetch(url)
        news_data = scrape_noticia(result)
        data.append(news_data)

    create_news(data)
    return data
