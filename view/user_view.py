import tkinter as tk
from tkinter import ttk

class UserView:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="User Information").pack()
        self.username_entry = ttk.Entry(self.root)
        self.username_entry.pack()
        self.email_entry = ttk.Entry(self.root)
        self.email_entry.pack()
        self.contact_info_entry = ttk.Entry(self.root)
        self.contact_info_entry.pack()
        self.submit_button = ttk.Button(self.root, text="Submit")
        self.submit_button.pack()
