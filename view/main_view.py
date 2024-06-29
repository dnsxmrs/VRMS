import customtkinter as c

class MainView:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        c.CTkLabel(self.root, text="Vehicle Renting Management System").pack(pady=10)
        self.add_button = c.CTkButton(self.root, text="Add Vehicle")
        self.add_button.pack(pady=10)
