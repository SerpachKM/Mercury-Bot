from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
import json
import os

# Динамически обновляемые переменные
driver = None
info_counterparty = []
link_counterparty = []
counterparty_name = []
num_repeats = 0
input_counterparty = []
found_links = []
action = []
counterarty_years = []
num_rep = []
max_matches = []

# Имя файла для хранения данных
CONFIG_FILE = "config.json"

# Значения по умолчанию
DEFAULT_CONFIG = {
    "link": "https://mercury.vetrf.ru/hs",
    "cmd": r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\temp\chrome-profile"',
    "name": "",
    "pass": "",
    "gos_login": "",
    "gos_pass": ""
}

url = DEFAULT_CONFIG["link"]
cmd_command = DEFAULT_CONFIG["cmd"]
username = DEFAULT_CONFIG["name"]
password = DEFAULT_CONFIG["pass"]
gos_login = DEFAULT_CONFIG["gos_login"]
gos_pass = DEFAULT_CONFIG["gos_pass"]

def load_config():
    """Загрузка конфигурации из файла."""
    global url, cmd_command, username, password, gos_login, gos_pass # Указываем, что обновляем глобальные переменные
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)  # Создаем файл, если его нет
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)

    # Обновляем глобальные переменные
    url = config.get("link", DEFAULT_CONFIG["link"])
    cmd_command = config.get("cmd", DEFAULT_CONFIG["cmd"])
    username = config.get("name", DEFAULT_CONFIG["name"])
    password = config.get("pass", DEFAULT_CONFIG["pass"])
    gos_pass = config.get("gos_pass", DEFAULT_CONFIG["gos_pass"])
    gos_login = config.get("gos_login", DEFAULT_CONFIG["gos_login"])

def save_config(config):
    """Сохранение конфигурации в файл."""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

def update_globals(config):
    """Обновление глобальных переменных."""
    global url, cmd_command, username, password, gos_pass, gos_login
    url = config.get("link", DEFAULT_CONFIG["link"])
    cmd_command = config.get("cmd", DEFAULT_CONFIG["cmd"])
    username = config.get("name", DEFAULT_CONFIG["name"])
    password = config.get("pass", DEFAULT_CONFIG["pass"])
    gos_pass = config.get("gos_pass", DEFAULT_CONFIG["gos_pass"])
    gos_login = config.get("gos_login", DEFAULT_CONFIG["gos_login"])

def view_config():
    """Просмотр текущей конфигурации."""
    print("Текущая конфигурация:")
    print(f"url: {url}")
    print(f"cmd_command: {cmd_command}")
    print(f"name: {username}")
    print(f"pass: {password}")
    print(f"gos_login: {gos_login}")
    print(f"gos_pass: {gos_pass}")

def update_config(key, value):
    """Обновление данных в файле конфигурации."""
    config = {}
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = json.load(f)
    config[key] = value
    save_config(config)
    load_config()  # Перезагружаем глобальные переменные
    print(f"Данные обновлены: {key} = {value}")

def info():
    global input_counterparty, num_repeats, counterparty_name, action, counterarty_years, num_rep, max_matches
    while True:
        try:
            if action == 2 or action == 3:
                counterparty_name = input('Название контрагента: ')
                num_repeats = int(input("Сколько раз выполнить действия на странице?: "))
                # Создаем список из названия контрагента, повторенного `num_repeats` раз
                input_counterparty = [counterparty_name] * num_repeats
                break

            elif action == 5:
                counterarty_years = input('Введите год выработки контрагента: ').strip()
                num_rep = int(input("Сколько раз выполнить действия на странице?: "))
                max_matches = int(input("Сколько совпадений обработать? (0 для обработки всех): "))
                break
        except ValueError:
            print("Пожалуйста, введите корректные данные.")
            continue

def connection():
    global driver
    try:
        # Настройка опций для браузера
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-popup-blocking")  # Отключение блокировки всплывающих окон
        options.add_argument("--start-maximized")        # Открытие окна на весь экран
        options.debugger_address = "127.0.0.1:9222"      # Указываем порт, на котором запущена отладка

        # Подключение к существующей сессии браузера
        driver = webdriver.Chrome(options=options)
        print("Соединение с браузером установлено.")
    except Exception as e:
        print(f"Ошибка при подключении к браузеру: {e}")

def open_chrome_with_debugging():
    try:
        akk = int(input('1 - Войти с помощью логина и пороля.\n2 - Войти через Госуслуги.\n -----------------> '))

        subprocess.Popen(f'start cmd /c "{cmd_command}"', shell=True)
        connection()

        time.sleep(2)
        driver.get(url)

        if akk == 1:
            time.sleep(2)
            log_pass = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "greyLink"))
            )
            log_pass.click()

            time.sleep(2)
            login = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "j_username"))
            )
            login.clear()
            login.send_keys(username)

            time.sleep(1)
            passw = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "j_password"))
            )
            passw.clear()
            passw.send_keys(password)

            time.sleep(2)
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "btn.login-btn.btn-success"))
            )
            button.click()
        elif akk == 2:
            log_pas = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href*="ESIARedirect"]'))
            )
            log_pas.click()

            time.sleep(2)
            log = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "plain-input"))
            )
            log.clear()
            log.send_keys(gos_login)

            time.sleep(1)
            pas = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "password"))
            )
            pas.clear()
            pas.send_keys(gos_pass)

            time.sleep(2)
            buttn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.plain-button_wide"))
            )
            buttn.click()
    except Exception as e:
        print(f'Ошибка: {e}')
        driver.quit()
