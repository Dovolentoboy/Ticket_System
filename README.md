## Запуск на вашем сервере

`1) tickets/ticket.py строка 24 и 25. Меняете айди на канал в котором будет сообщение с тикетом,затем меняете айди сообщения на то ,что после прописания команды !ticket_public` <br>
`2) tickets/ticket-control.py на строке 11 массив, меняете на айди ролей,которые смогу прописывать эту команду`  <br>
`3) buttons/create_ticket.py на строке 36 меняете айди категории в которой будет создан тикет`  <br>
`4) buttons/accept_ticket.py на строке 13 меняете айди на те,что меняли в tickets/ticket_control`  <br>
`5) buttons/control_panel.py на строке 145 меняете айди на канал в который будет прилетать лог с html страницой`  <br>
`6) modals/каждый файл в массиве roles меняете айди на те,что будут видеть канал при отправке модального окна`  <br>
 Также можете поменять эмбеды по вкусу  <br>
 ```pip install disnake```


# Цель работы

*Сделать качественную систему тикетов для сервера Даши*

## Функционал

*1) Эмбед с бесконечной кнопкой ✅<br>
*2) Кнопка,которая отвечает за создание канала с тикетом. Название канала : #ticket-{никнейм нажавшего} ✅ <br>
*3) Менюшка с выбором темы тикета ✅<br>
*4) Создание возможности написания сообщения ✅<br>
*5) Пинг ролей,которые отвечают за ответ в тему тикета ✅<br>
*6) Кнопка принятия тикета ✅<br>
*7) Команда ticket-control ✅<br>
*8) Сохранение всего чата в виде html страницы ✅ <br>
*9) Интеграция с модальными окнами ✅<br>

пиздец ✅


## Подробно о каждом пункте

## Эмбед с бесконечной кнопкой ✅
В канал Создания тикета публикуется эмбед,а внизу кнопка
В эмбеде будет написано :

Заголовок : Связь с персоналом
Описание : Чтобы связаться с персоналом нажмите на кнопку ниже
Цвет эмбеда : голубой #9aac23

## Кнопка,которая отвечает за создание канала с тикетом. Название канала : #ticket-{никнейм нажавшего} ✅

Цвет кнопки : зеленый
Функционал : создает канал с названием, забирает право писать , а также канал видит админы,кураторы и этот пользователь

## Менюшка с выбором темы тикета ✅
1)В канал тикета публикуется эмбед с выпадающим меню

2)Заголовок : Выберите тему тикета
3)Описание : После выбора темы с вами свяжется персонал нашего сервере,просьба подождать

4)Функционал :  Dropdown menu с темами тикета. После выбора темы,пользователь пишет своё сообщение

### Пинг ролей,которые отвечают за ответ в тему тикета ✅

Пингует в канале тикета роли,которы отвечают за тему

##  Кнопка принятия тикета   ✅

После пинга высылается кнопка с принятием, нажать на неё могут лишь определенные роли
Тому кто нажал выдается возможность писать в канал

##  Команда ticket-control ✅

Передать/закрыть тикет
При передаче высылается новая кнопка принять с пингом роли

При закрытии тикета исполняется функционал ниже

##  Сохранение всего чата в виде html страницы ✅

Сохраняет все сообщения из чата в виде html документа и отправляет его в определенный канал








