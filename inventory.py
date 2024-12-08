from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import f_info

def inventory():
    global product
    for _ in range(f_info.num_rep):
        try:
            product = int(input('1 - Скоропортящаяся продукция.\n2 - Не скоропортящаяся продукция.\n------------------->'))
            # Открываем меню
            menu = WebDriverWait(f_info.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "menu"))
            )
            menu.click()
            time.sleep(5)

            # Выполнение взаимодействий с элементами на странице
            placeholder = WebDriverWait(f_info.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "select2-selection__placeholder"))
            )
            placeholder.click()
            pyautogui.press('down', 1)
            pyautogui.press('enter')
            pyautogui.press('tab', 4, 2)
            pyautogui.press('enter', presses=2, interval=2)
            time.sleep(2)

            add_button = WebDriverWait(f_info.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "ui-button-text"))
            )
            add_button.click()
            inventory_search_matches(product)

        except Exception as e:
            print(f"Ошибка на этапе выполнения: {e}")

def inventory_search_matches(product):
    time.sleep(2)
    save_doc = WebDriverWait(f_info.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Добавить"))
    )
    save_doc.click()

    time.sleep(2)
    delete_radio = WebDriverWait(f_info.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='operation' and @value='3']"))
    )
    delete_radio.click()
    time.sleep(2)

    if product == 1:
        product_filter = WebDriverWait(f_info.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='perishable' and @value='true']"))
        )
        product_filter.click()
    elif product == 2:
        product_filter = WebDriverWait(f_info.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='perishable' and @value='withoutAnimal']"))
        )
        product_filter.click()
    time.sleep(2)

    log_button = WebDriverWait(f_info.driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "text"))
    )
    log_button.click()
    pyautogui.press('tab', 3)
    pyautogui.press('enter')
    time.sleep(3)

    # Поиск и обработка совпадений
    marked = 0
    while True:
        try:
            # Извлечение всех элементов с классом 'rtValue'
            elements = WebDriverWait(f_info.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'rtValue'))
            )
            if not elements:
                print("Элементы не найдены на странице.")
                time.sleep(2)
                break

            # Фильтрация совпадений по году
            for element in elements:
                if f_info.counterarty_years in element.text:
                    element.click()
                    print(f"Кликнул по элементу с текстом: {element.text}")
                    time.sleep(2)
                    marked += 1
                    if f_info.max_matches != 0 and marked >= f_info.max_matches:
                        break

            if f_info.max_matches != 0 and marked >= f_info.max_matches:
                print("Достигнуто максимальное количество совпадений.")
                time.sleep(2)
                save_2 = WebDriverWait(f_info.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "ui-button-text"))
                )
                save_2.click()
                time.sleep(2)
                break

            next_button = WebDriverWait(f_info.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[@title='перейти на следующую страницу']"))
            )
            next_button.click()
            print("Переход на следующую страницу.")
            continue
        except TimeoutError:
            print("Кнопка 'Следующая страница' не найдена. Завершение обработки.")
            break