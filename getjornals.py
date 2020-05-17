import urllib
import json
import re
import time
import sys
import os

from bs4 import BeautifulSoup

jornal_dict = {
    "Bola":"4137",
    "OJogo":"4138",
    "Record":"4139"
}

date = "-".join(sys.argv[1:])

def get_html_http(url):
    try:
        request = urllib.request.Request(url)
        html_bytes = urllib.request.urlopen(request).read()

        return html_bytes.decode("utf8")
    except Exception as e:
        # By writing to stdErr we can log this in the Flume logs
        sys.stderr.write("Error using urllib: " + str(e))
        sys.exit(-1)

for jornal in jornal_dict.keys():
    url = "https://24.sapo.pt/jornais/desporto/{0}/{1}".format(jornal_dict.get(jornal), date)
    html_str = get_html_http(url)
    soup = BeautifulSoup(html_str, features="lxml")

    picture_tag = soup.find_all("picture")[2]
    picture_url = picture_tag["data-original-src"]
    picture_title = picture_tag["title"].replace(" ","")
    
    path = "images/"+jornal.lower()+"/"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    urllib.request.urlretrieve(picture_url,path+"/"+picture_title.lower())