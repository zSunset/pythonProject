from bs4 import BeautifulSoup
import lxml

with open("blank/index.html", encoding='utf-8') as file:
    src = file.read()
# print(src)
soup = BeautifulSoup(src, 'lxml')

# title = soup.title
# print(title)
# print(title.text)
# print(title.string)

