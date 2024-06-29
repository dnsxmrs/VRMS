class Vehicle:
    def __init__(self, make, model, year, availability):
        self.make = make
        self.model = model
        self.year = year
        self.availability = availability

    def __repr__(self):
        return f"<Vehicle(make={self.make}, model={self.model}, year={self.year}, availability={self.availability})>"
