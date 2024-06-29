import tkinter as tk
from view.main_view import MainView
from controller.main_controller import MainController
from model.database import ensure_schema

def main():
    ensure_schema()  # Ensure the database schema is correct

    root = tk.Tk()
    root.title("Vehicle Renting Management System")
    root.geometry("800x600")
    
    # Initialize the main view and controller
    main_view = MainView(root)
    main_controller = MainController(main_view)
    
    # Example usage
    main_controller.add_vehicle("Toyota", "Camry", 2021, "Available")
    main_controller.add_user("johndoe", "johndoe@example.com", "123-456-7890")
    
    root.mainloop()

if __name__ == "__main__":
    main()
