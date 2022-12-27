import json

### задача 3
with open('operations.json', encoding='utf=8') as f:
    data = json.load(f)

cache = {}
sort_list = []  # значения даты

try:
    for i in data:
        x = int(i["date"].split('T')[0].replace('-', '') + i["date"].split('T')[1].split('.')[0].replace(':', ''))
        cache[x] = i
        sort_list.append(x)
except KeyError:
    print('')

top_fife = sorted(sort_list, reverse=True)[
           :int(input("Введите число последних транзакций: "))]  # получаю список сортированных дат от большей к меньшей
dict_res = []  # список для словарей с данными

for j in top_fife:  # прохожу циклом по датам и ищу совпадения в словаре cache где даты являются ключми
    display_res = {}  # словарь с данными о транзакции
    if j in cache:
        display_res[cache[j]['date'][:10].replace('-', '.')] = cache[j]['description']
        if 'from' not in cache[j] or 'to' not in cache[j]:  # если нет информации о переводе
            display_res["<откуда> -> <куда>"] = f"данные не указаны"
        else:
            name_card = cache[j]['from'].split(' ')[:-1]  # имя карты или счет
            from_ = f"{cache[j]['from'].split(' ')[-1][:6]}{'*' * (len(cache[j]['from'].split(' ')[-1]) - 10)}{cache[j]['from'].split(' ')[-1][-4:]}"  # замаскированные данные счета отправителя
            to_ = f"{'*' * (len(cache[j]['to'].split(' ')[-1]) - 4)}{cache[j]['to'].split(' ')[-1][-4:]}"
            display_res[f"{' '.join(name_card)} {from_}"] = f"-> {to_}"
        display_res[cache[j]['operationAmount']['amount']] = cache[j]['operationAmount']['currency']['name']
    dict_res.append(display_res)

if __name__ == "__main__":
    for i in dict_res:
        print('*' * 60)
        for z in i:
            print(z, i[z])
