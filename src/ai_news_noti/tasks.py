from GoogleNews import GoogleNews
import datetime
from typing import List
import requests
from src.ai_news_noti.constants import TELEGRAM_TOKEN, CHAT_ID
from loguru import logger
import multiprocessing


def get_news(topic:str) -> List[dict]:
    start_time = datetime.datetime.strftime(datetime.datetime.today(),"%m/%d/%Y")
    googlenews = GoogleNews(start= start_time,end = start_time, period = "24h",lang = "en")
    googlenews.search(f"{topic}")
    results = googlenews.results(sort = True)
    return results


def send_messages(message:str)-> dict:
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    response = requests.get(url,timeout=10).json()
    logger.info(response)

    return response



## to be fixed: need to mount EC2 to enable multiprocessing

def call_api(url:str):
    response = requests.get(url,timeout=10).json
    return response

def send_message_multi(news:list) -> dict:
    url_list = []
    for news in news:
        message = f"{news['title']}\n{news['link']}"
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        url_list.append(url)

    with multiprocessing.Pool(processes=5) as pool:
        results = pool.map(call_api, url_list)

    # Process the results
    for result in results:
        logger.info(result)