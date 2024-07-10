import customtkinter as ctk
from PIL import Image, ImageTk
import os

# create a class admin 
class Admin:
    def __init__(self, root):
        self.root = root

        self.selected_tile = None  # Track the currently selected tile
        self.create_widgets()

    def create_widgets(self):
        # create a sidebar with t
