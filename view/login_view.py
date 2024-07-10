import customtkinter as ctk
from PIL import Image, ImageTk
import os

class Login:
    def __init__(self, root):
        self.root = root

        self.selected_tile = None  # Track the currently selected tile
        self.create_widgets()

    def create_widgets(self):
        # Load the background image
        bg_image_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'images', '2.png')
        bg_image = Image.open(bg_image_path)
        bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
        bg_image_tk = ImageTk.PhotoImage(bg_image)

        # Set the background image
        self.bg_label = ctk.CTkLabel(self.root, image=bg_image_tk)
        self.bg_label.image = bg_image_tk  # Keep a reference to avoid garbage collection
        self.bg_label.place(relwidth=1, relheight=1)  # Make the label cover the entire window

        # Create the login frame
        frame_width = 400
        frame_height = 400
        self.login_frame = ctk.CTkFrame(self.root, fg_color='#FFFFFF', corner_radius=20, border_width=0,
                                        width=frame_width, height=frame_height)
        self.login_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        self.login_label = ctk.CTkLabel(self.login_frame, text="Login", font=("Arial", 24), fg_color='#FFFFFF')
        self.login_label.pack(pady=20)

        self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Username", corner_radius=10, border_width=0)
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Password", corner_radius=10, border_width=0, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(self.login_frame, text="Login", corner_radius=10, border_width=0, command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        # Add login logic here
        print("Login button clicked")

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("800x600")  # Set the window size as needed
    app = Login(root)
    root.mainloop()
