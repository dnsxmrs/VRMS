import tkinter as tk
from tkinter import ttk

class VehicleView:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Add a new vehicle").pack()
        self.make_entry = ttk.Entry(self.root)
        self.make_entry.pack()
        self.model_entry = ttk.Entry(self.root)
        self.model_entry.pack()
        self.year_entry = ttk.Entry(self.root)
        self.year_entry.pack()
        self.availability_entry = ttk.Entry(self.root)
        self.availability_entry.pack()
        self.submit_button = ttk.Button(self.root, text="Submit")
        self.submit_button.pack()
