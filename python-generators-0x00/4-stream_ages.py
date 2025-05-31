import mysql.connector

def stream_user_ages():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="ALX_prodev"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for (age,) in cursor:
        yield float(age)
    cursor.close()
    connection.close()

def average_age():
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    avg = total_age / count if count > 0 else 0
    print(f"Average age of users: {avg}")

