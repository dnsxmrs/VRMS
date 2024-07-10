import sqlite3
import os
from config.database_config import DATABASE_PATH, DATABASE_FOLDER

def get_db_connection():
    if not os.path.exists(DATABASE_FOLDER):
        os.makedirs(DATABASE_FOLDER)
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

def migrate_schema(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS VEHICLE(
                        VehicleID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Make TEXT NOT NULL,
                        Model TEXT NOT NULL,
                        Year INTEGER NOT NULL,
                        FuelType TEXT NOT NULL,
                        DailyRentalPrice REAL NOT NULL,
                        VehicleType TEXT NOT NULL,
                        AvailabilityStatus TEXT NOT NULL,
                        CreatedBy INTEGER,
                        FOREIGN KEY (CreatedBy) REFERENCES EMPLOYEE(EmployeeID))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS USERS(
                        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Email TEXT UNIQUE NOT NULL,
                        UserName TEXT UNIQUE NOT NULL,
                        FirstName TEXT NOT NULL,
                        MiddleName TEXT,
                        LastName TEXT NOT NULL,
                        Suffix TEXT,
                        PhoneNumber TEXT,
                        StreetAddress TEXT,
                        Brgy TEXT,
                        City TEXT,
                        Zipcode TEXT,
                        AccountCreationDate DATE NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS CAR(
                        VehicleID INTEGER PRIMARY KEY,
                        BodyStyle TEXT NOT NULL,
                        TransmissionType TEXT NOT NULL,
                        NumberOfDoors INTEGER NOT NULL,
                        FOREIGN KEY (VehicleID) REFERENCES VEHICLE(VehicleID))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS TRUCK(
                        VehicleID INTEGER PRIMARY KEY,
                        PayLoadCapacity REAL NOT NULL,
                        TruckBedSize TEXT NOT NULL,
                        NumberOfAxles INTEGER NOT NULL,
                        FOREIGN KEY (VehicleID) REFERENCES VEHICLE(VehicleID))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS MOTORCYCLE(
                        VehicleID INTEGER PRIMARY KEY,
                        EngineDisplacement REAL NOT NULL,
                        Type TEXT NOT NULL,
                        FOREIGN KEY (VehicleID) REFERENCES VEHICLE(VehicleID))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE(
                        EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
                        EmpEmail TEXT UNIQUE NOT NULL,
                        EmpUserName TEXT UNIQUE NOT NULL,
                        EmpPassword TEXT NOT NULL,
                        EmpFirstName TEXT NOT NULL,
                        EmpMiddleName TEXT,
                        EmpLastName TEXT NOT NULL,
                        EmpSuffix TEXT,
                        EmpPhoneNumber TEXT NOT NULL,
                        EmployeeType TEXT NOT NULL,
                        CreatedBy INTEGER,
                        FOREIGN KEY (CreatedBy) REFERENCES EMPLOYEE(EmployeeID))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS RESERVATION(
                        ReservationID INTEGER PRIMARY KEY AUTOINCREMENT,
                        VehicleID INTEGER NOT NULL,
                        EmployeeID INTEGER NOT NULL,
                        UserID INTEGER NOT NULL,
                        ReservationDate DATE NOT NULL,
                        RentalStartDate DATE NOT NULL,
                        RentalEndDate DATE NOT NULL,
                        TotalCost REAL NOT NULL,
                        Status TEXT NOT NULL,
                        FOREIGN KEY (UserID) REFERENCES USERS(UserID),
                        FOREIGN KEY (VehicleID) REFERENCES VEHICLE(VehicleID),
                        FOREIGN KEY (EmployeeID) REFERENCES EMPLOYEE(EmployeeID))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS INVOICE(
                        InvoiceID INTEGER PRIMARY KEY AUTOINCREMENT,
                        ReservationID INTEGER NOT NULL,
                        InvoiceDate DATE NOT NULL,
                        FOREIGN KEY (ReservationID) REFERENCES RESERVATION(ReservationID))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS PAYMENT(
                        PaymentID INTEGER PRIMARY KEY AUTOINCREMENT,
                        InvoiceID INTEGER NOT NULL,
                        PaymentAmount REAL NOT NULL,
                        PaymentMethod TEXT NOT NULL,
                        FOREIGN KEY (InvoiceID) REFERENCES INVOICE(InvoiceID))''')

def ensure_schema():
    conn = get_db_connection()
    cursor = conn.cursor()
    migrate_schema(cursor)
    conn.commit()
    conn.close()
