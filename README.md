# Система управления Mercury

## Описание

Данный проект предназначен для управления ветеринарными документами, учета инвентаризации и выполнения
различных действий в системе Mercury. Предоставляется удобный интерфейс для авторизации, возврата и погашения 
документов, работы с инвентаризацией и управления настройками.

## Возможности

- **Управление аккаунтом**: Авторизация в системе Mercury с помощью логина и пароля или через Госуслуги.
- **Работа с документами**: Возврат и погашение ветеринарных документов.
- **Учет инвентаря**: Обработка скоропортящейся и не скоропортящейся продукции.
- **Управление конфигурацией**: Просмотр, изменение и удаление настроек конфигурации.
- **Настраиваемость**: Использование файла `config.json` для хранения параметров.

## Файлы проекта

1. **`main.py`**: Главный файл программы, предоставляющий пользовательский интерфейс для всех функций.
2. **`f_info.py`**: Утилиты для работы с конфигурациями, подключения к браузеру и глобальными переменными.
3. **`veterinary_documents.py`**: Функции для возврата и погашения ветеринарных документов.
4. **`inventory.py`**: Модуль для учета инвентаря, включая работу с разными типами продукции.
5. **`config.json`**: Файл настроек, содержащий URL системы Mercury, данные для входа и параметры браузера.

## Требования

### Необходимое программное обеспечение

- Python 3.x
- Браузер Google Chrome
- Selenium
- PyAutoGUI

### Установка библиотек Python

Установите необходимые библиотеки с помощью команды:
```
pip install -r requirements.txt
```

## Системные требования

- Установленный браузер Google Chrome.
- ChromeDriver соответствующей версии браузера.

## Как использовать

1. Настройка конфигурации:
- Откройте файл config.json и задайте необходимые параметры, такие как логин, пароль и путь к браузеру.

2. Запуск программы: Выполните следующую команду в терминале:
```bash
python main.py
```

3. Выберите действие: При запуске программы вам будет предложено меню для выполнения различных действий:

- Авторизация.
- Возврат документов.
- Погашение документов.
- Управление настройками.
- Работа с инвентаризацией.

4. Работа с Mercury: Следуйте инструкциям в интерфейсе для выполнения операций. Все действия выполняются через браузер Google Chrome с использованием Selenium.

## Структура файла `config.json`

- link: URL системы Mercury.
- cmd: Команда для запуска браузера с поддержкой удаленной отладки.
- name и pass: Логин и пароль для входа в Mercury.
- gos_login и gos_pass: Логин и пароль для входа через Госуслуги.
 
# Замечания

- Убедитесь, что версия ChromeDriver соответствует установленной версии Google Chrome.
- Программа может запрашивать ввод данных в процессе работы (например, название контрагента или тип продукции).
- Все действия в браузере автоматизированы, но для их успешного выполнения необходимы корректные начальные настройки.

При возникновении проблем обратитесь к документации Selenium или убедитесь в актуальности ваших учетных данных.

