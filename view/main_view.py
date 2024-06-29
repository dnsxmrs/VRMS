import tkinter as tk
from tkinter import ttk

class MainView:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Vehicle Renting Management System").pack()
        self.add_button = ttk.Button(self.root, text="Add Vehicle")
        self.add_button.pack()
