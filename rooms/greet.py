import datetime

def salutation():
    cur = datetime.datetime.now().time()
    if cur.hour < 12:
        return 'Bom dia'
    elif cur.hour > 18:
        return 'Boa noite'
    else:
        return 'Boa tarde'
