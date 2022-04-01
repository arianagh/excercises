# import re
# import hashlib
#
#
#
# class Account():
#     def __init__(self, username, password, phone_number, email):
#         pattern_username = (r'(^[a-zA-Z]+_[a-zA-Z]+[a-zA-Z]$)')
#         if re.match(pattern_username,username):
#             self.username = username
#         else:
#             raise Exception('invalid username')
#
#         pattern_password = (r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}$')
#         if re.match(pattern_password,password):
#             password = password.encode('utf-8')
#             self.password = hashlib.sha256(password).hexdigest()        # it returns a hash object
#         else:
#             raise Exception('invalid password')
#
#         p1 = (r'^[^1,8]+[0-9]{11,}$')
#         p2 = (r'^09[1-9]{9}$')
#         if re.match(p2,phone_number):
#             self.phone_number = phone_number
#         if re.match(p1,phone_number):
#             self.phone_number = phone_number.replace('98','0')
#         else:
#             raise Exception('invalid phone number')
#
#         pattern_mail = (r'(^[a-zA-Z.-_/d]+@[a-zA-Z.-_/d]+\.[a-zA-Z]{2,5}$)')
#         if re.match(pattern_mail,email):
#             self.email = email
#         else:
#             raise Exception('invalid Email')
#
#
# user1 = Account('arian_aghaee', 'arA12bfsdfsd', '091212353211','arian@aghaee.com')
#
#
#
# class Site():
#     def __init__(self, url, register_users, active_users):
#         self.url = url
#         self.register_users = []
#         self.active_users = []
#
#
#     def register(self,user):
#         username = user.username
#         if username in self.register_users:
#             raise Exception('user already registered')
#         else:
#             self.register_users.append(username)
#         return 'register successful'
#
#
#     # def login(self):
#
#
#     def logout(self,user):
#         if user in self.active_users:
#             self.active_users.remove(user)
#             return 'logout successful'
#         else:
#             return 'not logged in!'
#
#
# d = Site('www.google.com',[],[])
# Site.register(d,user1)