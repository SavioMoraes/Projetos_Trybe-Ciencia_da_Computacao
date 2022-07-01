from tech_news.database import search_news
import time


# Requisito 6
def search_by_title(title):
    # busca por title, ignorando case sensitivo:
    # fonte:
    # https://stackoverflow.com/questions/7101703/how-do-i-make-case-insensitive-queries-on-mongodb
    title_query = search_news({"title": {"$regex": title, "$options": "i"}})
    data = []
    for news in title_query:
        data.append((news["title"], news["url"]))
    return data


# Requisito 7
def search_by_date(date):
    try:
        # o método .strptime, recebe uma data em sormato de string e
        # retorna ou no formato gmtime() ou localtime().
        # fonte: https://www.tutorialspoint.com/python/time_strptime.htm
        time.strptime(date, '%Y-%m-%d')
        date_query = search_news({"timestamp": {"$regex": date}})
        data = []
        for news in date_query:
            data.append((news["title"], news["url"]))
        return data

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    source_query = search_news({"sources": {
        "$regex": source, "$options": "i"
    }})
    data = []
    for news in source_query:
        data.append((news["title"], news["url"]))
    return data


# Requisito 9
def search_by_category(category):
    news_category = search_news({"categories": {
        "$regex": category, "$options": "i"
    }})
    news = []
    for news_item in news_category:
        fresh_news = (news_item["title"], news_item["url"])
        news.append(fresh_news)
    return news
