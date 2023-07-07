# Цель работы

*Сделать качественную систему тикетов для сервера Даши. Чтобы она не нуждалась в ticket-tool*
*А ну и еще я хочу сделать её чуть-чуть счастливее . Да-да ,Никитка*

## Функционал

1) Эмбед с бесконечной кнопкой ✅
2) Кнопка,которая отвечает за создание канала с тикетом. Название канала : #ticket-{никнейм нажавшего} ✅
3) Менюшка с выбором темы тикета ✅
4) Создание возможности написания сообщения ✅
5) Пинг ролей,которые отвечают за ответ в тему тикета ✅
6) Кнопка принятия тикета ✅
7) Команда ticket-control ✅
8) Сохранение всего чата в виде html страницы 🔃 - пиздец ✅
9) Интеграция с модальными окнами 🔃


## Подробно о каждом пункте

### Эмбед с бесконечной кнопкой 🔃
В канал Создания тикета публикуется эмбед,а внизу кнопка
В эмбеде будет написано :

Заголовок : Связь с персоналом
Описание : Чтобы связаться с персоналом нажмите на кнопку ниже
Цвет эмбеда : голубой #9aac23

### Кнопка,которая отвечает за создание канала с тикетом. Название канала : #ticket-{никнейм нажавшего} 🔃

Цвет кнопки : зеленый
Функционал : создает канал с названием, забирает право писать , а также канал видит админы,кураторы и этот пользователь

### Менюшка с выбором темы тикета 🔃
В канал тикета публикуется эмбед с выпадающим меню

Заголовок : Выберите тему тикета
Описание : После выбора темы с вами свяжется персонал нашего сервере,просьба подождать

Функционал :  Dropdown menu с темами тикета. После выбора темы,пользователь пишет своё сообщение

### Пинг ролей,которые отвечают за ответ в тему тикета 🔃

Пингует в канале тикета роли,которы отвечают за тему

### Кнопка принятия тикета   🔃

После пинга высылается кнопка с принятием, нажать на неё могут лишь определенные роли
Тому кто нажал выдается возможность писать в канал

### Команда ticket-control 🔃

Передать/закрыть тикет
При передаче высылается новая кнопка принять с пингом роли

При закрытии тикета исполняется функционал ниже

### Сохранение всего чата в виде html страницы 🔃

Сохраняет все сообщения из чата в виде html документа и отправляет его в определенный канал





