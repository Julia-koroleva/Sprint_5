import random
import string

class User:
    def __init__(self, email=None, password=None, name=None, mist_pass=None):
        self.email = email
        self.password = password
        self.name = name
        self.mist_pass = mist_pass
    
    def generate(self):
        if self.email is None and self.password is None and self.name is None and self.mist_pass is None:
            email_length = random.randint(5, 10)
            email_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=email_length))
            self.email = email_name + "@yandex.ru"
            
            password_length = random.randint(8, 12)
            password_chars = string.ascii_letters + string.digits + "!@#$%^&*"
            self.password = ''.join(random.choices(password_chars, k=password_length))
        
            mist_pass_length = random.randint(0, 5)
            mist_pass_chars = string.ascii_letters 
            self.mist_pass = ''.join(random.choices(mist_pass_chars, k=mist_pass_length))

            name_length = random.randint(5, 20)
            name_name = ''.join(random.choices(string.ascii_letters, k=name_length))
            self.name = name_name
        return self.email, self.password, self.name, self.mist_pass
    
    def clear(self):
        self.email = None
        self.password = None
        self.name = None
        self.mist_pass = None
    
    @classmethod
    def create_random_user(cls):
        user = cls()
        user.generate()
        return user

