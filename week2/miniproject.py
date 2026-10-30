import json
FILE = "expenses.json"

#Напиши функцию load_data(path): если файла нет, она возвращает пустой список, а не падает. Подсказка: FileNotFoundError.
def load_expenses():
    try:
        with open(FILE, 'r',encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)



def add_expense(expenses):
    expenses_dict = {}
    try:

        print('Введите: Название, сумму и категорию трат:')
        title = input("Название: ").strip()
        amount_text = input("Сумма: ")
        category = input("Категория: ").strip().lower()
        if title == '' or category == '':
            print('Неверное введеное значение')
            return None
        if float(amount_text) <= 0:
            print("Неверное числовое значение траты")
            return None
        expenses_dict['title'] = title
        expenses_dict['amount'] = float(amount_text)
        expenses_dict['category'] = category
        expenses.append(expenses_dict)
        save_expenses(expenses)

    except ValueError:
        print('Ввод неправильный')

# expenses1 = load_expenses()
# add_expense(expenses1)
# add_expense(expenses1)
# print(load_expenses())


def show_expenses(expenses):
    if len(expenses) == 0:
        print('Трат пока нет.')
    else:
        total_amount = 0
        for indx,i in enumerate(expenses,start=1):
            print(f"{indx}. {i['title']} — {i['amount']} ({i['category']})")
            total_amount += i["amount"]
        print(f"Всего: {total_amount}")




# test = [
#     {"title": "Кофе", "amount": 250.0, "category": "еда"},
#     {"title": "Метро", "amount": 60.0, "category": "транспорт"},
# ]
# show_expenses(test)    # две строки и итог 310.0
# show_expenses([])      # «Трат пока нет.» и никаких ошибок



def total_by_category(expenses, category):
    total = 0
    for k in expenses:
        if k['category'] == category:
            total += k['amount']
    return total




def main():
    expenses = load_expenses()
    while True:
        print('----------menu----------')
        print('1 - Добавить трату')
        print('2 — показать все')
        print('3 - сумма по категории')
        print('4 — выход')
        n = input('Выберите пункт меню: ')
        if n == '1':
            add_expense(expenses)
        elif n == '2':
            show_expenses(expenses)

        elif n == '3':
            cat = input('Введите категорию товара: ').strip().lower()
            total = total_by_category(expenses, cat)
            print(f"Сумма по категории «{cat}»: {total}")

        elif n == '4':
            break
        else:
            print('Выбран неверный пункт меню. Повторите попытку')

if __name__ == "__main__":
        main()