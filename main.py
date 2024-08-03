from src.ai_news_noti.tasks import get_news, send_messages
from loguru import logger

def handler(event, context) -> dict:
    news_results = get_news("AI")

    if news_results:
        for news in news_results:
            send_messages(f"{news['title']}\n{news['link']}")

    return {
        "statusCode":200,
        "body":"success"
    }


if __name__ == "__main__":
    res = handler(None,None)
    logger.info(res)