import customtkinter as c

class VehicleView:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        c.CTkLabel(self.root, text="Add a new vehicle").pack(pady=10)
        self.make_entry = c.CTkEntry(self.root, placeholder_text="Make")
        self.make_entry.pack(pady=5)
        self.model_entry = c.CTkEntry(self.root, placeholder_text="Model")
        self.model_entry.pack(pady=5)
        self.year_entry = c.CTkEntry(self.root, placeholder_text="Year")
        self.year_entry.pack(pady=5)
        self.availability_entry = c.CTkEntry(self.root, placeholder_text="Availability")
        self.availability_entry.pack(pady=5)
        self.submit_button = c.CTkButton(self.root, text="Submit")
        self.submit_button.pack(pady=10)
