from clickhouse_connect import get_client

client = get_client(host = 'localhost' , port = 8123 , username = 'default' , database = 'AdityaDB')

# Update orders
try:
	client.command("""
		ALTER TABLE orders
		UPDATE amount = 147
		WHERE user_id = 5
	""")
	print("Updated user_id = 5 amount to 147")
except Exception as e:
	print("Update Fialed:  ",e)
