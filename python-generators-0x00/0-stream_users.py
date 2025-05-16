import seed

connection = seed.connect_db()

def stream_users():
  if connection:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
      yield row
    cursor.close()
    connection.close()

for users in stream_users():
  print(users)