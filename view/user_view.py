import customtkinter as c

class UserView:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        c.CTkLabel(self.root, text="User Information").pack(pady=10)
        self.username_entry = c.CTkEntry(self.root, placeholder_text="Username")
        self.username_entry.pack(pady=5)
        self.email_entry = c.CTkEntry(self.root, placeholder_text="Email")
        self.email_entry.pack(pady=5)
        self.contact_info_entry = c.CTkEntry(self.root, placeholder_text="Contact Info")
        self.contact_info_entry.pack(pady=5)
        self.submit_button = c.CTkButton(self.root, text="Submit")
        self.submit_button.pack(pady=10)
