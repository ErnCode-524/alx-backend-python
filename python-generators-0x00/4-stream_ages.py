import seed

connection = seed.connect_db()
cursor = connection.cursor()

def stream_user_ages():
  if connection:
    cursor.execute('SELECT * FROM user_data')
    rows = cursor.fetchall()
    for row in rows:
      yield row

def average_age():
  total = 0
  count = 0
  for user in stream_user_ages():
    print(user)
    total += user[3]
    count += 1
  avg_age = total / count
  print(f'Average age of users: {avg_age}')

average_age()