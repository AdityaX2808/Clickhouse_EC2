import clickhouse_connect

client = clickhouse_connect.get_client(
	host = 'localhost' ,
	database = 'AdityaDB' ,
	username = 'default' 
)

print(client.ping())
