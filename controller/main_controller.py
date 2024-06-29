from model.database import get_db_connection
from controller.vehicle_controller import VehicleController
from controller.user_controller import UserController

class MainController:
    def __init__(self, view):
        self.view = view
        self.conn = get_db_connection()
        self.vehicle_controller = VehicleController(self.conn)
        self.user_controller = UserController(self.conn)

    def add_vehicle(self, make, model, year, availability):
        self.vehicle_controller.add_vehicle(make, model, year, availability)

    def add_user(self, username, email, contact_info):
        self.user_controller.add_user(username, email, contact_info)
