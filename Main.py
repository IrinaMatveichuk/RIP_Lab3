import ChildClass
from datetime import datetime

user = ChildClass.Client("http://api.vk.com/method", 'users.get')
user.param = 'user_ids='+input("Введите username или id пользователя: ")
resp = user.execute()
id = user.find_id(resp)

friend = ChildClass.Client('http://api.vk.com/method', 'friends.get')
friend.param = "user_id="+str(id)+"&fields=bdate"
friends = friend.execute()

friend_dict = friends.get('response')
dictf = friend.count_friend(friend_dict)
friend.print_dict(dictf)
