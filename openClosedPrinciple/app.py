import requests
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup as soup
import csv 


class Portal(ABC):
    URL = ''
    NAME = ''
    TYPES = []

    def html_soup(self):
        client = requests.get(self.URL)
        page_html = client.content
        client.close()
        return soup(page_html, 'html.parser')

    @abstractmethod
    def get_news_url(element):
        """ Must be overridden """
        pass

    @abstractmethod
    def get_news_title(elements):
        """ Must be overridden """
        pass

    @abstractmethod
    def html_to_array(self):
        """ Must be overridden """
        pass

    def write_on_csv(self, delimiter=';', output=None):
        if not output:
            output = self.NAME + '.csv'
        keys = self.html_to_array()[0].keys()
        with open(output, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys, delimiter=delimiter)
            dict_writer.writeheader()
            dict_writer.writerows(self.html_to_array())


class OGlobo(Portal):
    NAME = 'oglobo' 
    URL = 'http://globo.com'
    TYPES = [('Principal','hui-premium__title'),('Secundário','hui-highlight-title')]

    @staticmethod
    def get_news_url(element):
        while(element.parent.get('href') is None and bool(element.parent)):
            element = element.parent
        if not element.parent:
            raise Exception('URL not found')
        return element.parent.get('href')
    
    @staticmethod
    def get_news_title(element):
        return element.text
    
    def html_to_array(self):
        news_array = []
        for _type in self.TYPES:
            elements = self.html_soup().findAll('p', {'class': _type[1]})
            for element in elements:
                news_array.append(
                    {
                        'Tipo': _type[0],
                        'Notícia': self.get_news_title(element),
                        'Link': self.get_news_url(element)
                    }
                )
        return news_array  