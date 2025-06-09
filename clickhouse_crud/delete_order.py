from clickhouse_connect import get_client

client = get_client(host = 'localhost' , port = 8123 , username = 'default' , database = 'AdityaDB')

#Delete order
try:
	client.command("""
		ALTER TALBE orders
		DELETE WHERE order_id = 101
	""")
	print("Deleted order with order_id = 101. ")
except Exception as e:
	print("Deletion failed...")
