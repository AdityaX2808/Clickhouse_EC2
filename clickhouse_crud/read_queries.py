from clickhouse_connect import get_client

client = get_client(host = 'localhost' , port = 8123 , database = 'AdityaDB' , username = 'default')

# Get users
print("All Users:")
users = client.query("SELECT * FROM users").result_rows
for row in users:
	print(row)


# Get orders
print("All Orders:")
orders = client.query("SELECT * FROM orders").result_rows
for row in orders:
	print(row)
