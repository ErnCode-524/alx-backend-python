import seed

connection = seed.connect_db()
cursor = connection.cursor()

def paginate_users(page_size, offset):
    cursor.execute(f'SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}')
    rows = cursor.fetchall()
    connection.close
    return rows

user_data = paginate_users(10, 0)

count = 0
for user in user_data:
    print(user)
    count += 1
print(count)    