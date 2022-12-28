import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    # метод для сбора данных с переданного сайта
    def scrape(self):
        # отправляет запрос на сайт и возвращает объект Response с html-кодом сайта и дополнительные данные
        r = urllib.request.urlopen(self.site)
        # функция response.read() возвращает html
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        count = 0
        # поиск всех URL-адресов (тег <а>) в загруженном html-коде
        # при каждом прохождении цикла переменной tag присваивается значение нового объекта Tag, у которого есть
        # много переменных экземпляра класса, но выбирает только переменную href
        for tag in sp.find_all("a"):
            # получаем URL
            url = tag.get("href")
            if url is None:
                continue

            if "http" in url:
                count +=1
                print("\n" + url)
        print(count)



if __name__ == '__main__':
    news = "https://news.rambler.ru/"
    Scraper(news).scrape()