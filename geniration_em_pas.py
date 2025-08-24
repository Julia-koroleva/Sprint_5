import random
import string

class User:
    def __init__(self, email=None, password=None, name=None):
        self.email = email
        self.password = password
        self.name = name
    
    def generate(self):
        if self.email is None and self.password is None:
            email_length = random.randint(5, 10)
            email_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=email_length))
            self.email = email_name + "@yandex.ru"
            
            password_length = random.randint(8, 12)
            password_chars = string.ascii_letters + string.digits + "!@#$%^&*"
            self.password = ''.join(random.choices(password_chars, k=password_length))
        
            name_length = random.randint(5, 10)
            name_name = string.ascii_letters
            self.name = name_name
        return self.email, self.password, self.name
    
    def clear(self):
        self.email = None
        self.password = None
        self.name = None
    
    @classmethod
    def create_random_user(cls):
        user = cls()
        user.generate()
        return user

