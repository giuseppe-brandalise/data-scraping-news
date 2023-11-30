from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    title = title.lower()
    results = search_news({"title": {"$regex": title}})

    return [(searched["title"], searched["url"]) for searched in results]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
