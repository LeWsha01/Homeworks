def converter(list_currency, f, n, s):
    if s == 'RUB':
        result = (list_currency[f] * n) / list_currency[s] * 100
    elif f == 'RUB':
        result = (list_currency[f] * n) / list_currency[s] / 100
    elif s == 'BYN':
        result = n * list_currency[s]
    elif f == 'BYN':
        result = n / list_currency[s]
    else:
        result = (list_currency[f] * n) / list_currency[s]
    return round(result, 2)


