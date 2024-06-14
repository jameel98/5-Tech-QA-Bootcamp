class User:
    def __init__(self, username, name, age, email):
        self.username = username
        self.name = name
        self.age = age
        self.email = email

    def to_dict(self):
        return {
            'username': self.username,
            'name': self.name,
            'age': self.age,
            'email': self.email
        }
