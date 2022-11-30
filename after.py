import requests 
from bs4 import BeautifulSoup 
import time 
from datetime import datetime
import re
t= int(input("Введите срок между проверками(секундах): "))
n=1 
Z=1 
while True:
    Z=1
    date = datetime.today()#Настройка времени и даты 
    now_time=date.strftime('%H:%M')
    day = datetime.now().date()
    while Z== 1:
        #МГНОВЕННЫЙ СБОР НЫНЕШНЕГО КУРСА ВАЛЮТ
        DOLLAR_= ('https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4')
        #!!!!!!!!!!!найти в гуглу "my user agent" и вставить в {"User-Agent":"СЮДА"}!!!!!!!!!!!!!!
        headers_ ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}
        full_page_ = requests.get(DOLLAR_, headers=headers_)	
        soup_ = BeautifulSoup(full_page_.content, 'html.parser')
        convert_ = soup_.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})#конвертирование 
        was = str(convert_[0])
        was = re.findall(r'\d+\.\d+', was)
        was = float(was[0])
        Z -=1

    print("№",n,"\n","Was:  ", was," rubles ",now_time," ",day)#СЧИТЫВАЕМ КУРС ПРОШЛОГО ВРЕМЕНИ М СОХРАНЯЕМ ЕГО В ПЕРЕМЕННУЮ was
    n +=1
    time.sleep(t)#ВРЕМЯ ОЖИДАНИЯ, КОТОРОЕ УКАЗАЛ ПОЛЬЗОВАТЕЛЬ ПЕРЕД НАЧАЛОМ ВЫПОЛНЕНИЯ ПРОГРАММЫ

    #СБОР НОВОГО КУРСА ВАЛЮТ
    DOLLAR_RUB = ('https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4')
    headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}
    full_page = requests.get(DOLLAR_RUB, headers=headers)	
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})#конвертирование 
    NOW = str(convert[0])
    NOW = re.findall(r'\d+\.\d+', NOW)
    NOW = float(NOW[0])#ФОРМАТИРОВАНИЕ ЧИСЛА
    
    date = datetime.today()#Настройка времени и даты 
    now_time_1=date.strftime('%H:%M')
    day_1 = datetime.now().date()
    
    print("Now: ",NOW," rubles ",now_time_1," ",day_1,"       Difference: ",NOW-was)
    print("-------------------------------------------------------------------------------------------")
    r = NOW-was
    with open ("do_aftet.txt","a") as f:
        st=" "
        text= ("№",n,"\n","Was:  ", was," rubles ",now_time," ",day,"\n","Now: ",NOW," rubles ",now_time_1," ",day_1,"    Difference: ",r,"\n","-------------------------------------------------------------------------------------------","\n")
        for string in text:
            st += str(string)
        f.write(st)
   
