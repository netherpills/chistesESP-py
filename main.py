from bs4 import BeautifulSoup
import requests

response = requests.get('http://www.chistes.com/ChisteAlAzar.asp?n=3')
soup = BeautifulSoup(response.text, "html.parser")
chiste = soup.find("div", "chiste").text

print(chiste)
