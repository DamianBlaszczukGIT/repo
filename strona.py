import requests
from bs4 import BeautifulSoup
import os
from duckduckgo_search import DDGS
import time
from markdownify import markdownify as md

def fetch_info(query):
    time.sleep(5)
    site_query = f"{query} site:wikipedia.org"
    results = DDGS().text(site_query, max_results=1)
    return results

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
    
    image = 'https://www.tiobe.com' + columns[3].find('img')['src']
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
    content += f"  - [More Info](./{item['name'].replace(' ', '_')}.md)\n"
    
    # Create a subpage for each item with only the "Info" section
    subpage_content = f"---\n"
    subpage_content += f"title: {item['name']}\n"
    subpage_content += f"---\n\n"
    subpage_content += f"# {item['name']}\n"
    subpage_content += f"- **Info**:\n"
    for result in item['info']:
        subpage_content += f"  - [{result['title']}]({result['href']}): {md(result['body'])}\n"
    
    with open(f"{item['name'].replace(' ', '_')}.md", 'w', encoding='utf-8') as subfile:
        subfile.write(subpage_content)

main_content = f"---\n"
main_content += f"title: TIOBE Index for March 2025\n"
main_content += f"---\n\n"
main_content += h1.text + '\n'
for paragraph in paragraphs:
    main_content += paragraph + '\n'

for item in data:
    main_content += f"### {item['name']}\n"
    main_content += f"![Image]({item['image']})\n"
    main_content += f"- **Usage**: {item['usage']}\n"
    main_content += f"- **Change**: {item['change']}\n"
    main_content += f"- **Info**:\n"
    main_content += f"  - [More Info](./{item['name'].replace(' ', '_')}.md)\n"

with open('tiobe.md', 'w', encoding='utf-8') as file:
    file.write(main_content)

print('Done!')