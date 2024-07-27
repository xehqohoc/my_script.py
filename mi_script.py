import requests
from bs4 import BeautifulSoup

url = 'https://www.geeksforgeeks.org/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extraer todos los enlaces (URLs)
for link in soup.find_all('a'):
    print(link.get('href'))
  
