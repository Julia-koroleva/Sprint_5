import random
import string

class User:
    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password
    
    def generate(self):
        if self.email is None and self.password is None:
            email_length = random.randint(5, 10)
            email_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=email_length))
            self.email = email_name + "@yandex.ru"
            
            password_length = random.randint(8, 12)
            password_chars = string.ascii_letters + string.digits + "!@#$%^&*"
            self.password = ''.join(random.choices(password_chars, k=password_length))
        
        return self.email, self.password

