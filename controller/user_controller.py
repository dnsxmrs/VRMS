class UserController:
    def __init__(self, conn):
        self.conn = conn

    def add_user(self, username, email, contact_info):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users (username, email, contact_info) VALUES (?, ?, ?)",
                        (username, email, contact_info))
        self.conn.commit()
