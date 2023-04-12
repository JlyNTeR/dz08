from datetime import datetime, timedelta, date
from collections import defaultdict
from pprint import pprint

def get_next_week_start(d: datetime):
    diff_days = 7 - d.weekday()
    return d + timedelta(days=diff_days)
    pass

def prepare_birthday(text: str):
    bd = datetime.strptime(text, '%d, %m, %Y')
    return bd.replace(year=datetime.now().year).date()

def get_birthdays_per_week(users):
    
    birthdays = defaultdict(list)

    today = datetime(2023, 3, 13).date() #datetime.now().date()

    next_week_start = get_next_week_start(today)
    start_period = next_week_start - timedelta(2)
    end_period = next_week_start + timedelta(4)

    happy_users = [user for user in users if start_period <= prepare_birthday(user['birthday']) <= end_period]
    
    
    for user in happy_users:
        current_bd = prepare_birthday(user['birthday'])
        if current_bd.weekday() in (5,6):
            birthdays['Monday'].append(user['name'])
        else:
            birthdays[current_bd.strftime('%A')].append(user['name'])
    return birthdays

if __name__ == '__main__':
    
    users = [{'name': 'Yehor', 'birthday': '15, 3, 1992'},
            {'name': 'Vasyl', 'birthday': '16, 3, 1992'},
            {'name': 'Petya', 'birthday': '17, 3, 1992'},
            {'name': 'Kolya', 'birthday': '18, 3, 1992'},
            {'name': 'Stepan', 'birthday': '19, 3, 1992'},
            {'name': 'Petro', 'birthday': '20, 3, 1992'},
            {'name': 'Stas', 'birthday': '21, 3, 1992'},
            {'name': 'Ivan', 'birthday': '22, 3, 1992'}]
    result = get_birthdays_per_week(users)
    pprint(result)