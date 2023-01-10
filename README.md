# DOLLAR_MONITORING<
<div id="header" align="center">
  <img src="https://media.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" width="100"/>
</div>



EN
==


RU
==
Программа получения курса валют с Google 

ЦЕЛЬ
==
Программа может быть полезна для отслеживания валют в заданном времени, при том сохраняет результат в читабельном виде: записывает курс валюты, время, разницу.
Вывод сумму, равную одному доллару США 

НАПРИМЕР
===
Запустим нашу программа:
>![image](https://user-images.githubusercontent.com/79650307/211669765-b2a38b76-9b9f-47ce-9efc-d231e54e9786.png)
>Программа спрашивает, через сколько секунд(целое число) будут обновляться данные.В нашем случае - через 2 секунды.
>Потом ждёт введённое нами время и снова получает информацию, выводит в окно консоли и сохраняет результат в файл do_after.txt
>![image](https://user-images.githubusercontent.com/79650307/211670535-f24f15f8-c461-42cc-9fa6-c9a33bb85bbc.png)

>ВАЖНО: программа будет работать бесконечно, пока будет работать интернет и пока запущена программа.Для завершения программы - закройте окно консоли
>![image](https://user-images.githubusercontent.com/79650307/211671003-186bb825-759f-40db-8d3f-8f4363ae00af.png)

ОБРАБОТКА ОШИБОК
==
Получение ошибки минимизировано.Ошибка может возникнуть только при заполнении промежутка времени.
Если пользователь ввёл, например, букву - программа завершит работу:
>![image](https://user-images.githubusercontent.com/79650307/211672598-92d00b56-342a-4d00-b77e-8611c2f10b61.png)



