class User:
    def __init__(self, username, email, contact_info):
        self.username = username
        self.email = email
        self.contact_info = contact_info

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email}, contact_info={self.contact_info})>"
