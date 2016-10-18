import requests
import BaseClass
from datetime import datetime

class Client(BaseClass.BaseClient):
    param = None

    def __init__(self, url, methods):
        self.BASE_URL = url
        self.method = methods

    def generate_url(self, method):
        return '{0}/{1}'.format(self.BASE_URL, method)

    def _get_data(self, method):
        response = requests.get(self.generate_url(method), self.param)
        return response.json()

    def find_id(self, inf):
        try:
            id1 = inf.get('response')
            id = id1[0].get('uid')
        except:
            print("Не удалось найти пользователя")
            exit()
        return id

    def def_age(self, str_date):
        try:
            bdate = datetime.strptime(str_date, '%d.%m.%Y')
        except: return None

        day_now = datetime.now().day
        month_now = datetime.now().month
        year_now = datetime.now().year

        age = year_now - bdate.year
        if (bdate.month == month_now and bdate.day > day_now) or bdate.month > month_now:
            age -= 1
        return age

    def count_friend(self, friends_dict):
         if (friends_dict == None):
             print ('Страница пользователя удалена или заблокирована')
             exit()
         if (len(friends_dict) == 0):
             print ("У пользователя нет друзей, либо они скрыты")
             exit()
         friends_count = {'Не указан возраст у: ':0}
         for friend in friends_dict:
             bdate = friend.get('bdate')
             age = self.def_age(bdate)
             if (age == None):
                 friends_count['Не указан возраст у: '] += 1
                 continue
             if (friends_count.get(age) == None):
                 friends_count[age] = ''
             friends_count[age] += '#'
         return friends_count

    def print_dict(self, dict):
        print('Не указан возраст у: ', dict['Не указан возраст у: '])
        del dict['Не указан возраст у: ']
        for key in sorted(dict):
            print(key, ': ', dict[key])







