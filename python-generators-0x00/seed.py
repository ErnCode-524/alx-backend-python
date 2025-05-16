import mysql.connector

def connect_db():
  try:
    connection = mysql.connector.connect(
      host = 'localhost',
      user = 'root',
      password = 'Naakmp@30.',
      database = 'ALX_prodev'
    )
    print('Connected to the database successfully!')
    return connection
  
  except mysql.connector.Error as err:
    print('Failed to connect to the database.')
    print('Error:', err)
    return None
  
connect_db()