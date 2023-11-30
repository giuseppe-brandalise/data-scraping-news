from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from unittest.mock import patch


def test_reading_plan_group_news():
    news = [
        {
            "url": "https://blog.betrybe.com/carreira/noticialinkedin",
            "title": "linkedin",
            "timestamp": "02/02/2002",
            "writer": "Carlos Drummon de Andrade",
            "reading_time": 14,
            "summary": "linkedin ta em alta como sempre",
            "category": "Carreira",
        },
        {
            "url": "https://blog.betrybe.com/tecnologia/noticiagpt",
            "title": "gpt",
            "timestamp": "20/20/2020",
            "writer": "Jeff Bezos",
            "reading_time": 23,
            "summary": "Amazon e gpt fazem aliança",
            "category": "Tecnologia",
        },
        {
            "url": "https://blog.betrybe.com/tecnologia/noticiajs",
            "title": "javascript",
            "timestamp": "13/13/2013",
            "writer": "Senhor Js",
            "reading_time": 15,
            "summary": "js é bom",
            "category": "Tecnologia",
        },
    ]

    err = "Valor 'available_time' deve ser maior que zero"
    with pytest.raises(ValueError, match=err):

        ReadingPlanService.group_news_for_available_time(-20)

    with patch(
        "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy",
        return_value=news,
    ):
        result = ReadingPlanService.group_news_for_available_time(15)
        assert len(result["readable"]) == 2
        assert len(result["unreadable"]) == 1

        assert result == {
            "readable": [
                {
                    "unfilled_time": 1,
                    "chosen_news": [("linkedin", 14)],
                },
                {
                    "unfilled_time": 0,
                    "chosen_news": [("javascript", 15)],
                }
            ],
            "unreadable": [("gpt", 23)],
        }
