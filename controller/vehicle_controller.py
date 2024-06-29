class VehicleController:
    def __init__(self, conn):
        self.conn = conn

    def add_vehicle(self, make, model, year, availability):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO vehicles (make, model, year, availability) VALUES (?, ?, ?, ?)",
                    (make, model, year, availability))
        self.conn.commit()
