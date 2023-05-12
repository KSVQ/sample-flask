class User:
    def __init__(self, user_data):
        self.id = user_data[0]
        self.first_name = user_data[1]
        self.last_name = user_data[2]
        self.email = user_data[3]
        self.password = user_data[4]
        self.role = user_data[5]
        self.theme = user_data[6]

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
