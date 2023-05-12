import mysql.connector

class TnxDB:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="217.21.66.128",
            user="u225557959_tnxtests",
            password="6OmNHE0*ilym6w8M",
            database="u225557959_tnxtests"
        )
        self.cursor = self.conn.cursor()

    def insert_user(self, first_name, last_name, email, password):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        values = (first_name, last_name, email, password)
        self.cursor.execute(query, values)
        self.conn.commit()

    def update_user(self, user_id, first_name=None, last_name=None, email=None, password=None):
        query = "UPDATE users SET "
        values = []
        if first_name:
            query += "first_name = %s, "
            values.append(first_name)
        if last_name:
            query += "last_name = %s, "
            values.append(last_name)
        if email:
            query += "email = %s, "
            values.append(email)
        if password:
            query += "password = %s, "
            values.append(password)
        query = query[:-2] + " WHERE id = %s"
        values.append(user_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id = %s"
        values = (user_id,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_users(self):
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_user_by_id(self, user_id):
        query = "SELECT * FROM users WHERE id = %s"
        values = (user_id,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()
    
    def get_user_by_email(self, email):
        query = "SELECT * FROM users WHERE email = %s"
        values = (email,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()




# db = TnxDB()

# # Insert a new user
# db.insert_user("John", "Doe", "johndoe@example.com", "password")

# # Update an existing user
# db.update_user(1, email="newemail@example.com")

# # Delete a user
# db.delete_user(1)

# # Retrieve all users
# users = db.get_users()
# for user in users:
#     print(user)

# # Retrieve a specific user by ID
# user = db.get_user(2)
# print(user)
