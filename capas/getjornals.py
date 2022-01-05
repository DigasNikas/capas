import urllib
import os
import datetime

from dateutil import parser
from bs4 import BeautifulSoup

class GetJornals:

    jornal_dict = {
        "Bola":"4137",
        "OJogo":"4138",
        "Record":"4139"
    }

    def __get_html_http(self, url):
        try:
            request = urllib.request.Request(url)
            html_bytes = urllib.request.urlopen(request).read()

            return html_bytes.decode("utf8")
        except Exception as e:
            sys.stderr.write("Error using urllib: " + str(e))
            sys.exit(-1)

    def get_jornal(self, jornal, date):
        url = "https://24.sapo.pt/jornais/desporto/{0}/{1}".format(self.jornal_dict.get(jornal), date)
        html_str = self.__get_html_http(url)
        soup = BeautifulSoup(html_str, features="lxml")
        picture_tag = soup.find_all("picture")[6]
        picture_url = picture_tag["data-original-src"]
        picture_title = picture_tag["title"].replace(" ","")
        
        path = "images/"+jornal.lower()+"/"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        urllib.request.urlretrieve(picture_url,path+"/"+picture_title.lower())
        
    def get_jornals(self, date):
        for jornal in self.jornal_dict.keys():
            self.get_jornal(jornal, date)

    def get_jornals_range(self, start, end):
        start_dt = parser.parse(start)
        end_dt = parser.parse(end)
        while start_dt < end_dt:
            self.get_jornals(start_dt.strftime('%Y-%m-%d'))
            start_dt = start_dt + datetime.timedelta(days=1)

    def __init__(self) -> None:
        pass
