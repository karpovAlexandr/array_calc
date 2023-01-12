# Калькулятор массивов (int only)

## Tехнические требования к проекту:

Необходимо разработать сервис rest api с интерфейсом openapi/swagger ui, который на входе будет получать файл json
формата со списком цифр, обратно пользователю направлять сумму всех цифр.
Пример json файла:
``
{
"array": ["1", "2", "3", "4", null]
}``

Реализовать с помощью двух методов:

1) Синхронный
2) Асинхронный (пользователь получает ID сессии и получает ответ по ID сессии). Реализовать простую схему хранения
   сессии и результата
   Весь код должен запускаться в виде докер сервиса.
   Дополнить руководством по запуску.

## Стек:

1. python3.10
2. fastapi
3. postgresql12+

## Процесс разворачивания проекта:

- скачиваем и устанавливаем докер для нашей ОС (https://docs.docker.com/get-docker/)
- git clone {repo_url}
- запускаем скрипт build_app.sh
- проект будет доступен на 5000 порту по адресу нашего хоста