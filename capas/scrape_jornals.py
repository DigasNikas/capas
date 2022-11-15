import urllib.request
import os
import datetime
import sys

from dateutil import parser
from bs4 import BeautifulSoup
from sqlalchemy import insert, create_engine
from sqlalchemy.orm import sessionmaker
from capas.models import JornalURL

class GetJornals:

    engine = create_engine('postgresql://root:root@localhost/root')
    Session = sessionmaker(bind=engine)
    session = Session()

    jornal_dict = {
        "bola":"4137",
        "ojogo":"4138",
        "record":"4139"
    }

    def insert_jornal(self, name, desc, url, date_tmsp, date_str, path):
        jornal = JornalURL(name=name, description=desc, url=url, timestamp=date_tmsp, date=date_str, path=path)
        self.session.merge(jornal)

    def __get_html_http(self, url):
        try:
            request = urllib.request.Request(url)
            html_bytes = urllib.request.urlopen(request).read()

            return html_bytes.decode("utf8")
        except Exception as e:
            sys.stderr.write("Error using urllib: " + str(e))
            sys.exit(-1)

    def get_jornal(self, jornal, datetime):
        date = datetime.strftime('%Y-%m-%d')
        url = "https://24.sapo.pt/jornais/desporto/{0}/{1}".format(self.jornal_dict.get(jornal), date)
        html_str = self.__get_html_http(url)
        soup = BeautifulSoup(html_str, "html.parser")
        picture_tag = soup.find_all("picture")[1]
        description = soup.find_all("section", {"class": "headlines"})
        if len(description) > 0:
            description = description[0].get_text()
        else:
            description = ""
        picture_url = picture_tag["data-original-src"]
        picture_title = picture_tag["title"].replace(" ","")
        
        path = "images/"+jornal+"/"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        image_path = path+date.lower()
        urllib.request.urlretrieve(picture_url,image_path)

        self.insert_jornal(picture_title,description,picture_url,datetime,date,image_path)
        
    def get_jornals(self, date):
        for jornal in self.jornal_dict.keys():
            self.get_jornal(jornal, date)

    def get_jornals_range(self, start, end):
        start_dt = parser.parse(start)
        end_dt = parser.parse(end)
        while start_dt < end_dt:
            self.get_jornals(start_dt)
            start_dt = start_dt + datetime.timedelta(days=1)
        self.session.commit()

    def __init__(self) -> None:
        pass
