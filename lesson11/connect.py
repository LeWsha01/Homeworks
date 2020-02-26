def connect(response):
    lst = response.json()
    lst1 = []
    lst2 = []
    for val in lst:
        lst1.append(val.get('Cur_Abbreviation'))
        lst2.append(val.get('Cur_OfficialRate'))
    list_currency = {key: value for key, value in zip(lst1, lst2)}

    return list_currency