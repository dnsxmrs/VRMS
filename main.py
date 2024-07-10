import customtkinter as c
from view.login_view import Login
from controller.main_controller import MainController
from model.database import ensure_schema

def main():
    ensure_schema()  # Ensure the database schema is correct

    root = c.CTk()
    root.title("Vehicle Renting Management System")
    root.geometry("1366x768")
    root.resizable(False, False)
    c.set_appearance_mode("Light")
    
    # Initialize the main view and controller
    Login(root)
    MainController(root)



    root.mainloop()

if __name__ == "__main__":
    main()
