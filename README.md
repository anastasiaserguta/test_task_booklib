# BOOKLIB DJANGO Python 3.12.2

Проект создан в рамках подачи заявки на стажировку IT Bootcamp.

**Порядок запуска:**
1) создание и активация виртуального окружения, клонирование репозитория (git clone --depth=1 --single-branch -b dev https://github.com/anastasiaserguta/test_task_booklib.git ) из ветки dev (там находится рабочая локальная версия, ветка main используется для размещения проекта на облачном хостинге);
2) установка в виртуальное окружение зависимостей из requirements.txt (команда -> pip freeze install requirements.txt);
3) запуск программы стандарным для джанго способом (python manage.py runserver);
4) веб-сервис развернут по следующей ссылке [https://anastasiaserguta.pythonanywhere.com/] (тестирование прав модератора: логин - test_moderator, пароль - test1999).

***

**Основной функционал:**
1. BookLib представляет собой веб-сервис для работы с данными о книгах и авторах.
2. Основные страницы веб-сервиса представлены в виде шаблонов:
***главная (/home)*** - выводит список всех доступных в базе книг, с указанием авторов и жанров, позволяет перейти по клику на название книги либо имя автора к детальному представлению книги, автора (включая список имеющихся на сервере книг автора);
***авторы (/authors)*** - выводит таблицу всех доступных в базе авторов, с указанием их имени и уникального ID, доступен переход по клику на имя автора к карточке с детальным представлением информации об авторе;
***книги (/books)*** - вывод таблицу всех доступных книг с указанием их названия, года издания и уникального ID (данные остортированы в алфавитном порядке);
***поиск (/search)*** - позволяет осуществлять поиск книг и авторов, переходить в их конкретному представлению, а также знакомиться с доступными на сервисе жанрами;
***добавить запись (/create)*** - доступна только авторизованным пользователям (всем) и позволяет добавлять новые данные на сервис (авторов, книги, жанры), необходимо сохранять определенный порядок при добавлении книги, ввиду комплексности ее значений (Many-to-Many): 1 шаг - добавление автора, 2 шаг - добавление жанра, 3 шаг - добавление книги. !!! ВАЖНО: с одной книги может ассоциировано 1 и более авторов, а также 1 и более жанр. Вместе с тем удаление автора не влечет удаления книги;
***вход/регистрация*** - реализует авторизацию и регистрацию пользователей;
***профиль/выход*** - позволяют пользователям просматривать свой профиль, редактировать его, в том числе менять пароль, а также выходить из аккаунта;
***детальные представления книг, авторов*** - содержат полную информацию об авторах и книгах, предусмотрена возможность их редактирования/удаления (доступна только пользователям с правами модератора, которые предоставляет администратор сайта);
***о веб-сервисе (/about)*** - предзначен для размещения информации о сервисе.

***
-- UI/UX дизайн выполнен с использованием Bootstrap5 --












***



