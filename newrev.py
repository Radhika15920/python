import pyodbc

# Establish connection between python and sql server
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-PPOFI28\SQLEXPRESS02;"
    "Database=Reservation;"
    "Trusted_Connection=yes;")
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Read from text file
with open('read_file.txt', 'w') as file:
    cursor.execute("SELECT * FROM Passengers")
    for row in cursor:
        file.write(str(row))
file = open("read_file.txt","r")
lines =file.readlines()
for line in lines :
    print(line)
    
# Extract data from text file
Extract_line = [line.split() for line in lines]
print(Extract_line)

#  Function to check if train already exists in Database otherwise insert
def function(train_id):
    cursor.execute("SELECT * FROM Trains WHERE train_id = ?", (train_id,))
    train_exists = cursor.fetchone()
    if train_exists:
        print("\nTrain exists ID(train_id):",train_exists)
    else:
        print("No train found with ID (train_id)")

cursor.execute("SELECT COUNT(*) FROM Trains")
total_train = cursor.fetchone()[0]
print("\nTotal number of trains:", total_train)
cursor.execute("SELECT * FROM Trains WHERE train_id = 111")
train_exists = cursor.fetchone()
print("\nTrain exists (ID 111):", train_exists)
if train_exists:  
    print("Train 111 already exists, skipping insert.")
else:
    insert_train_query = "INSERT INTO Trains (train_id, train_name, train_number) VALUES (111, 'kashi2', 902768)"
    cursor.execute(insert_train_query)
    conn.commit()
    print("Train 111 inserted.")

#calling of function to check whether train_id exists or not
function(101)
function(102)

# Fetch available trains
cursor.execute("SELECT train_name FROM Trains")
trains = cursor.fetchall()
for train in trains:
    print(train)  
train_name = input("Enter Train Name:")
if train_name in train:
    print("You selected train:", train_name)
else:
    print("Train name does not exist.")

# Fetch available seats
cursor.execute("SELECT seat_id FROM Seats")
all_seats = cursor.fetchall()
print("\nTotal Seat IDs:")
for seat in all_seats:
    print(seat)

cursor.execute("SELECT seat_id FROM Reservations")
reserved_seats =  cursor.fetchall()
print("\nReserved Seat IDs:")
for seat in reserved_seats:
    print(seat)

print("\nAvailable Seat IDs:")
for seat in all_seats:
    if seat not in reserved_seats:
        print(seat)

# confirm reservation
passenger_id= input("Enter passenger_id:")
seat_choice = input("Enter available seat_id:")
if seat_choice in all_seats and seat_choice not in reserved_seats:
    cursor.execute("INSERT INTO Reservations (passenger_id, seat_id) VALUES (?, ?)", (passenger_id, seat_choice))
    conn.commit()
    print("Reservation confirmed for {passenger_name} on seat {seat_choice}.")
elif seat_choice in reserved_seats:
    print("That seat is already reserved.")
else:
    print("Invalid seat ID entered.")


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

insert_train_query = '''INSERT INTO Trains(train_id, train_name, train_number) VALUES(?,?,?,)'''


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
print("Seat Availability for Train ID {train_id}:")
for row in cursor.fetchall():
    print("Train Name: {row.train_name}")
    print("Total Seats: {row.total_seats}")
    print("Reserved Seats: {row.reserved_seats}")
    print("Available Seats: {row.available_seats}")    

cursor.close()
conn.close()



