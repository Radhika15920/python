import pyodbc

conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-PPOFI28\SQLEXPRESS02;"
    "Database=Reservation;"
    "Trusted_Connection=yes;")

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT * FROM Trains")
trains = cursor.fetchall()
print("Trains:")
for row in trains:
    print(row)
cursor.execute("SELECT * FROM Seats")
seats = cursor.fetchall()
print("\nSeats:")
for row in seats:
    print(row)
cursor.execute("SELECT * FROM Passengers")
passengers = cursor.fetchall()
print("\nPassengers:")
for row in passengers:
    print(row)
cursor.execute("SELECT * FROM Reservations")
reservations = cursor.fetchall()
print("\nReservations:")
for row in reservations:
    print(row) 

train_id = 106
train_name = 'SuperExpress'
train_number = 14580
insert_train_query = """INSERT INTO Trains (train_id, train_name, train_number)VALUES (?, ?, ?)"""
cursor.execute("SELECT * FROM Trains")
trains = cursor.fetchall()
print("\nTrains:")
for row in trains:
    print(row)

train_id= 108
train_name= 'shatabdi express'
train_number= 453749

insert_train_query = '''''''INSERT INTO Trains(train_id, train_name, train_number) VALUES(?,?,?,)'''''''
cursor.execute('SELECT * FROM Trains')
trains= cursor.fetchall()
print("\nTrains:")
for row in trains:
    print(row)

train_id = 104 
sql_query = f"""SELECT t.train_id, t.train_name, COUNT(s.seat_id) AS total_seats, COUNT(r.seat_id) AS reserved_seats,
COUNT(s.seat_id) - COUNT(r.seat_id) AS available_seats FROM Trains t
JOIN 
    Seats s ON t.train_id = s.train_id
LEFT JOIN 
    Reservations r ON s.seat_id = r.seat_id
WHERE
    t.train_id = {train_id} 
GROUP BY 
    t.train_id, t.train_name; """
cursor.execute(sql_query)
print(f"Seat Availability for Train ID {train_id}:")
for row in cursor.fetchall():
    print(f"Train Name: {row.train_name}")
    print(f"Total Seats: {row.total_seats}")
    print(f"Reserved Seats: {row.reserved_seats}")
    print(f"Available Seats: {row.available_seats}")    

cursor.close()
conn.close()



