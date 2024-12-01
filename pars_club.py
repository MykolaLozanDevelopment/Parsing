import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.101.76 Safari/537.36"
}

def download(url):
    response = requests.get(url, stream=True)
    with open("C:\\GITHUB\\Parsing\\image\\" + url.split("/")[-1], "wb") as r:
        for value in response.iter_content(1024 * 1024):
            r.write(value)
        


def get_url():
    for count in range(1, 7):
        url = f"https://scrapingclub.com/exercise/list_basic/page=1?page={count}"
        respons = requests.get(url, headers=headers)
        soup = BeautifulSoup(respons.text, "lxml")
        data = soup.find_all("div", class_="w-full rounded border")

        for d in data:
            card_url = "https://scrapingclub.com" + d.find("a").get("href")
            yield card_url


def array():
    for card_url in get_url():
        sleep(1)
        response = requests.get(card_url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_="my-8 w-full rounded border")

        url_img = "https://scrapingclub.com" + data.find(
            "img", class_="card-img-top"
        ).get("src")
        name = data.find("h3", class_="card-title").text.replace("\n", "")
        price = data.find("h4", class_="my-4 card-price").text
        description = data.find("p", class_="card-description").text
        download(url_img)
        yield name, price, description, url_img
