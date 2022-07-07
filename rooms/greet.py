import datetime

def salutation():
    cur = datetime.datetime.now().time()
    if cur.hour < 12:
        return 'Good morning'
    elif cur.hour > 18:
        return 'Good night'
    else:
        return 'Good afternoon'
