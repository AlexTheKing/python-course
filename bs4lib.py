import requests
from bs4 import BeautifulSoup

page = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')

print("Raw:")
print(page.text)

soup = BeautifulSoup(page.text, 'html.parser')

print("Using soup:")
print(soup.prettify())

body = list(html.children)[3]
p = list(body.children)[1]

print("Parsed paragraph:", p.get_text())

print("Find all paragraphs:", soup.find_all('p'))

print("Using CSS selectors:", soup.select('p'))


