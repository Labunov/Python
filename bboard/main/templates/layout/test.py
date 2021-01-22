# def stack():
#     class D:
#         def show(self):
#             print('Метод')
#
#     obj1=D()
#     return obj1
#
#
# stack()
# d = stack()
# d.show()
# class D:
#     pass
# print()
import json
# nums = [2,3,45,100,1000]
# filename = 'nums.json'
# with open(filename,'w') as f:
#     json.dump(nums,f)
#
# filename = 'nums.json'
# with open(filename) as fi:
#     nums_new = json.load(fi)
#
# obj_py = nums_new
# print(type(nums_new))

# username = input('Введите ваше имя: ')
# filename = 'nums.json'
# with open(filename,'w',encoding="utf-8") as f:
#     json.dump(username,f,ensure_ascii=False)
#     print('мы запомним ваше имя как :'+username+'!!!')
# filename = 'user.json'
#
# try:
#     with open(filename,encoding="utf-8") as f:
#         user = json.load(f)
# except:
#     username = input('введите свое имя: ')
#     with open(filename,'w',encoding="utf-8") as fi:
#         json.dump(username,fi,ensure_ascii=False)
#         print("мы заомним ваше имя")
# else:
#     print('Добро пожаловать  ' + user)

def get_username():
    """Получает имя пользователя , если оно есть"""
    filename = 'user.json'
    try:
        with open(filename,encoding="utf-8") as f:
            user = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user

def greet_user():
    """Приветствие пользователя"""
    username = get_username()
    if username:
        print("Добро пожаловать " + username + "!!!")
    else:
        username = input("Введите свое имя: ")
        filename = 'user.json'
        with open(filename, 'w', encoding="utf-8") as fi:
            json.dump(username,fi,ensure_ascii=False)

greet_user()