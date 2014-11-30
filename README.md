###Тестовое задание на  позицию Junior Python Developer.

#####Цель тестового задания
Определить возможную динамику самообучения кандидата. А так же глубину понимания кода, реализующего тестовое задание.

#####Задание

Написать тестовое web-приложение по управлению электронной библиотекой:
1. Редактирование (доступно авторизованному пользователю при наличии аутентификации):
    -Управление списком книг: добавить / удалить / редактировать книгу.
    -Управление списком авторов: добавить / удалить / редактировать автора.
    -Запись о книге содержит следующие данные:  ID,  Название.
    -Запись об авторе содержит следующие данные:  ID, Имя.
    -Свзязь между книгами и авторами – многие ко многим.
2. Поиск книг по названию либо автору (доступно анонимному пользователю при наличии аутентификации).
3. Аутентификации и авторизация (по желанию кандидата).

#####Технологии, которые должны быть задействованы:
-Flask
-SQLAlchemy (Declarative)
-SQLite (встроенный в приложение)
-Jinja2 Templates
-WTForms
-jQuery (желательно, но возможно использование альтернативных решений)
Список может быть расширен по усмотрению кандидата, но с обязательным использованием технологий, перечисленных выше.

#####Дополнительные требования
1. Код проекта должен быть доступен на сервисе http://github.org или http://bitbucket.org.
2. Проект должен содержать SQL-скрипты для развертывания базы данных и наполнения ее тестовыми данными.
3. Пользовательские данные должны валидироваться перед сохранением в БД.