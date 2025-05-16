import seed

connection = seed.connect_db()
cursor = connection.cursor()

def stream_users_in_batches(batch_size):
    cursor.execute(f'SELECT * FROM user_data LIMIT {batch_size}')
    rows = cursor.fetchall()
    for row in rows:
      yield row

for user in stream_users_in_batches(5):
   print(user)

   print('*' * 100)

def batch_processing(batch_size):
   for user in stream_users_in_batches(batch_size):
      if user[3] > 25:
         print(user)
      else:
         print('I am below 25')
      
batch_processing(3)

cursor.close()
connection.close()