import f_info
import veterinary_documents
import inventory

def main():
    while True:
        try:
            f_info.load_config()  # Обновляет данные при запуске
            f_info.action = int(input('\n1 - Войти в аккаунт меркурий.\n2 - Возврат документов.\n3 - Погасить документы.\n4 - Данные.\n5 - Инвентаризация.\n6 - Инвентаризация уже созданой заявки.\n7 - Информация.\n8 - Выход.------------------>  '))
            if f_info.action == 1:
                f_info.open_chrome_with_debugging()
            elif f_info.action == 2:
                f_info.info()
                f_info.connection()
                veterinary_documents.return_doc()
            elif f_info.action == 3:
                f_info.info()
                f_info.connection()
                veterinary_documents.repayment_doc()
            elif f_info.action == 4:
                chek = int(input('1 - Просмотр данных.\n2 - Изменение данных.\n3 - Удаление данных.\n------------------>  '))
                if chek == 1:
                    f_info.view_config()
                elif chek == 2:
                    print(f'\n{f_info.view_config()}')
                    key = input('Введите наименование изменяемого параметра: ')
                    value = input('Введите новое значение: ')
                    f_info.update_config(key, value)
                elif chek == 3:
                    print(f'\n{f_info.view_config()}')
                    key = input('Введите наименование удаляемого параметра: ')
                    f_info.update_config(key, '')
            elif f_info.action == 5:
                f_info.info()
                f_info.connection()
                inventory.inventory()
            elif f_info.action == 6:
                f_info.info()
                f_info.connection()
                inventory.inventory_search_matches(f_info.product)
            elif f_info.action == 7:
                print('Создатель проекта: SerpachKM\nGitHub: https://github.com/SerpachKM')
                print('Подержать разработчика монеткой:\nT-Bank - 2200 7017 2644 9843\nРНКБ - 2200 0202 3670 0474')
            elif f_info.action == 8:
                break
        except Exception:
            print('\nВы ввели неверное значение')
            input('Enter для продолжения: ')

if __name__ == '__main__':
    main()