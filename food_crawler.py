import requests
from bs4 import BeautifulSoup
import os





url = "https://health-diet.ru/base_of_food/food_24507/"

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'https://www.google.ru/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')

tab = soup.find("table",{"class":"uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed"})

# наименование
a = tab.find_all('a')
category = list()
for it in a:
    newcat = it.get('title')
    category.append(newcat[len('Химический состав продукта: '):])

# параметры
tds = tab.find_all('td', attrs={"class":"uk-text-right"})
c = 0
tmp = ""
parameters = list()

for it in tds:
    value = it.string
    value = value.replace(' ', '')
    value = value.replace('г', '')
    value = value.replace('кКал', '')
    if (c == 3):
        tmp += value
        parameters.append(tmp)
        c = 0
        tmp = ""
        continue
    if (c < 3):
        tmp += value + ':'
        c += 1

c = 0

result = ""

for cat in category:
    d = ':'
    p = parameters[c].split(d)
    result += cat + d + p[1] + d + p[2] + d + p[3] + d + p[0] + d + "10" + "\n"
    c += 1

file = open("result.txt","w")
file.write(result)
file.close

print("результаты в файлике result.txt в этой же папке ))")
