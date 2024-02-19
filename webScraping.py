from bs4 import BeautifulSoup
import requests

URL = ""
page = requests.get(URL)

soup=BeautifulSoup(page.text,'html')
