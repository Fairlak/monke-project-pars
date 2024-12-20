from fastapi import FastAPI, Request
import requests
from bs4 import BeautifulSoup
from virtualenv.config.convert import NoneType

app = FastAPI()


@app.get("/get/name")
async def root(request: Request):
    try:
        link = request.headers.get('aniLink')
        all_data = requests.get(link)
        soup = BeautifulSoup(all_data.text, "html.parser")
        all_news = soup.find('div', class_='anime-title')
        anime = all_news.find('h1')
        return anime.string
    except:
        return 'not found'
        
