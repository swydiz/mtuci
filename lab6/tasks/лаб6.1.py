class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    def set_password(self, new_password):
        self.__password = new_password
    def check_password(self, password):
        return self.__password == password

a = UserAccount('AAA', 'aaa@gmail.com', 12345)
a.set_password(789)
print(a.check_password(789))
print(a.check_password(1234))
