import mysql.connector

# Global connection object
conn = None
cursor = None

# Connect to MySQL
def connect_db():
    global conn, cursor
    if conn is None or not conn.is_connected():
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sandy@2004",  # Change this to your MySQL password
            database="ev_charging"
        )
        cursor = conn.cursor()
        print("Connected to MySQL Successfully!")

# CREATE Operations
def add_user(name, vehicle_no):
    connect_db()
    query = "INSERT INTO users (name, vehicle_no) VALUES (%s, %s)"
    cursor.execute(query, (name, vehicle_no))
    conn.commit()
    print(f"User {name} with vehicle {vehicle_no} added successfully!")

def add_station(station_name, location):
    connect_db()
    query = "INSERT INTO stations (station_name, location) VALUES (%s, %s)"
    cursor.execute(query, (station_name, location))
    conn.commit()
    print(f"Station {station_name} added successfully!")

# READ Operations
def get_users():
    connect_db()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)

def get_stations():
    connect_db()
    cursor.execute("SELECT * FROM stations")
    stations = cursor.fetchall()
    for station in stations:
        print(station)

# UPDATE Operations
def update_user(user_id, new_name):
    connect_db()
    query = "UPDATE users SET name = %s WHERE user_id = %s"
    cursor.execute(query, (new_name, user_id))
    conn.commit()
    print(f"User ID {user_id} updated to {new_name}!")

def update_station(station_id, new_name):
    connect_db()
    query = "UPDATE stations SET station_name = %s WHERE station_id = %s"
    cursor.execute(query, (new_name, station_id))
    conn.commit()
    print(f"Station ID {station_id} updated to {new_name}!")

# DELETE Operations
def delete_user(user_id):
    connect_db()
    query = "DELETE FROM users WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    conn.commit()
    print(f"User ID {user_id} deleted successfully!")

def delete_station(station_id):
    connect_db()
    query = "DELETE FROM stations WHERE station_id = %s"
    cursor.execute(query, (station_id,))
    conn.commit()
    print(f"Station ID {station_id} deleted successfully!")

# Close Connection
def close_db():
    global conn, cursor
    if conn and conn.is_connected():
        cursor.close()
        conn.close()
        print("Database connection closed.")

# Example Execution (Uncomment to test)
# connect_db()
# add_user("Sandeep", "TN10AB5678")
# add_station("EV Charging Point 1", "Chennai - Anna Nagar")
# get_users()
# get_stations()
# update_user(1, "Sandeep Kumar")
# delete_station(1)
# close_db()
