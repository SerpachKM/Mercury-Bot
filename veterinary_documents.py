from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import f_info

def counterparties_processing():
    try:
        # Получаем информацию о контрагентах и ссылки
        f_info.info_counterparty = [element.text for element in f_info.driver.find_elements(By.CLASS_NAME, 'rtValue')]
        f_info.link_counterparty = [element.get_attribute("href") for element in f_info.driver.find_elements(By.CLASS_NAME, 'operation-link.blue') if element.get_attribute("href")]

        if not f_info.info_counterparty or not f_info.link_counterparty:
            raise ValueError("Не удалось получить информацию о контрагентах или ссылки.")

        inn_info_list = [item for item in f_info.info_counterparty if "ИНН:" in item]

        info_dict = {}
        key_counts = {}

        for key, value in zip(inn_info_list, f_info.link_counterparty):
            key_counts[key] = key_counts.get(key, 0) + 1
            numbered_key = f"{key}_{key_counts[key]}"
            info_dict[numbered_key] = value

        input_counterparty_counts = {}
        numbered_input_counterparty = []

        for key in f_info.input_counterparty:
            input_counterparty_counts[key] = input_counterparty_counts.get(key, 0) + 1
            numbered_input_counterparty.append(f"{key}_{input_counterparty_counts[key]}")

        # Поиск найденных элементов с учетом нумерации
        found_items = {key: info_dict[key] for key in numbered_input_counterparty if key in info_dict}
        f_info.found_links = [info_dict[key] for key in found_items]

        if not found_items:
            print("Не удалось найти контрагентов по заданному запросу.")
        else:
            for i in enumerate(found_items):
                print("Найденные элементы:", i)
            for o in enumerate(f_info.found_links):
                print("Ссылки на найденные контрагенты:", o)
            c = input('Нажмите Enter для продолжения: ')

    except ValueError as e:
        print(f"Ошибка: {e}")
    except KeyError as e:
        print(f"Ошибка: Ключ {e} не найден в словаре.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

def repayment_doc():
    try:
        # Выполняем действия для обработки контрагентов
        counterparties_processing()
        for link in f_info.found_links:
            try:
                # Открытие ссылки в новой вкладке
                time.sleep(2)
                f_info.driver.execute_script(f"window.open('{link}', '_blank');")
                time.sleep(2)

                f_info.driver.switch_to.window(f_info.driver.window_handles[-1])

                time.sleep(3)
                f_info.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                rep = WebDriverWait(f_info.driver, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "ui-button-text"))
                )
                rep.click()

                time.sleep(3)
                f_info.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                save_doc = WebDriverWait(f_info.driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "positive"))
                )
                save_doc.click()

                time.sleep(2)
            except Exception as e:
                print(f"Ошибка при обработке ссылки {link}: {e}")
            finally:
                # Закрытие текущей вкладки
                f_info.driver.close()

                # Переключение обратно на исходную вкладку
                if f_info.driver.window_handles:
                    f_info.driver.switch_to.window(f_info.driver.window_handles[0])
                else:
                    print("Все вкладки закрыты. Завершаем работу.")
                    break

    except Exception as e:
        print('Общая ошибка: ', e)

def return_doc():
    try:
        # Выполняем действия для обработки контрагентов
        counterparties_processing()
        for link in f_info.found_links:
            try:
                # Открытие ссылки в новой вкладке
                time.sleep(2)
                f_info.driver.execute_script(f"window.open('{link}', '_blank');")
                time.sleep(2)

                f_info.driver.switch_to.window(f_info.driver.window_handles[-1])

                time.sleep(3)
                f_info.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                rep = WebDriverWait(f_info.driver, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "ui-button-text"))
                )
                rep.click()

                time.sleep(3)
                f_info.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                checkbox = WebDriverWait(f_info.driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "splitWeight"))
                )
                checkbox.click()

                time.sleep(2)
                input_field = WebDriverWait(f_info.driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "inputWeight"))
                )
                input_field.clear()
                input_field.send_keys("0")

                save_doc = WebDriverWait(f_info.driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "positive"))
                )
                save_doc.click()

                time.sleep(2)
            except Exception as e:
                print(f"Ошибка при обработке ссылки {link}: {e}")
            finally:
                f_info.driver.close()

                if f_info.driver.window_handles:
                    f_info.driver.switch_to.window(f_info.driver.window_handles[0])
                else:
                    print("Все вкладки закрыты. Завершаем работу.")
                    break

    except Exception as e:
        print('Общая ошибка: ', e)
