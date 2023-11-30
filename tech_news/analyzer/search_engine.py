from tech_news.database import search_news, db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    title = title.lower()
    results = search_news({"title": {"$regex": title}})

    return [(searched["title"], searched["url"]) for searched in results]


# Requisito 8
def search_by_date(date):
    try:
        date_to_search = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )

        results = list(
            db.news.find(
                {"timestamp": {"$regex": date_to_search}},
                {"title": True, "url": True, "_id": False},
            )
        )

        return [(searched["title"], searched["url"]) for searched in results]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
