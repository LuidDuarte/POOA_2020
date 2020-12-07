import requests
from bs4 import BeautifulSoup as soup 

class GetNews:
    def __init__(self, name, url, types):
        self.name = name
        self.url = url
        self.types = types

    @staticmethod
    def get_news_url(element):
        while(element.parent.get('href') is None and bool(element.parent)):
            element = element.parent
        if not element.parent:
            raise Exception('URL not found')
        return element.parent.get('href')

    def html_soup(self):
        client = requests.get(self.url)
        page_html = client.content
        client.close()
        return soup(page_html, 'html.parser')

    def return_news(self,elements):
        news_array = []
        for element in elements:
            news = {'title': element.text, 'link': self.get_news_url(element)}
            news_array.append(news)
        return news_array

    def return_from_types(self):
        news = []
        for _type in self.types: #_types instead types because types is a keyword
            news_type = {}
            news_type['type'] = _type[0]
            elements = self.html_soup().findAll('p', {'class': _type[1]})
            news_from_type = self.return_news(elements)
            news_type['data'] = news_from_type
            news.append(news_type)
        return news

    def write_on_csv(self, delimiter=';', output=None):
        if not output:
            output = self.name + '.csv'
        file = open(output, 'w')
        news_array = self.return_from_types()
        file.write("Tipo"+delimiter+"Notícia"+delimiter+"Link\n")
        for _type in news_array:
            for news in _type['data']:
                file.write(_type['type']+delimiter)
                file.write(news['title']+delimiter+news['link']+'\n')

