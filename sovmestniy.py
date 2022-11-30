import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
from datetime import datetime
import re

DOLLAR_RUB = ('https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4')
headers ={"User-Agent":"ЗАГУГЛИ МАЙ ЮЗЕР АГЕНТ")


full_page = requests.get(DOLLAR_RUB, headers=headers)	
soup = BeautifulSoup(full_page.content, 'html.parser')

ti= int(input("срок проверки(сек!)):"))
while True: 

   
	convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})#конвертирование 
	was = str(convert[0])
	was = re.findall(r'\d+\.\d+', was)
	was = float(was[0])
	print("ЩАс курс :",was)
	time.sleep(ti)

	