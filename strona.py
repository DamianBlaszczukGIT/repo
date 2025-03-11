import requests
from bs4 import BeautifulSoup
import os
from duckduckgo_search import DDGS
import time

def fetch_info(query):
    time.sleep(1)
    site_query = f"{query} site:wikipedia.org"
    results = DDGS().text(site_query, max_results=1)
    print(results)

url = 'https://www.tiobe.com/tiobe-index/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

h1 = soup.find('h1')

paragraphs = []
for paragraph in h1.find_next_siblings():
    if paragraph.name == 'p':
        paragraphs.append(paragraph.text)
    elif paragraph.name == 'h2':
        break

table = soup.find('table')

rows = table.find('tbody').find_all('tr')

data = []
for row in rows:
    columns = row.find_all('td')
    
    image = columns[3].find('img')['src']
    name = columns[4].text.strip()
    usage = columns[5].text.strip()
    change = columns[6].text.strip()
    info = fetch_info(name)

    data.append({
        'image': image,
        'name': name,
        'usage': usage,
        'change': change,
        'info': info
    })

content = h1.text + '\n'
for paragraph in paragraphs:
    content += paragraph + '\n'

for item in data:
    content += f"### {item['name']}\n"
    content += f"![Image]({item['image']})\n"
    content += f"- **Usage**: {item['usage']}\n"
    content += f"- **Change**: {item['change']}\n"
    content += f"- **Info**:\n"
    content += f"- {item['info']}\n"

with open('tiobe.md', 'w', encoding='utf-8') as file:
    file.write(content)

print('Done!')