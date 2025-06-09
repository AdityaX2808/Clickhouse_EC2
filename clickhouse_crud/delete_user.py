from clickhouse_connect import get_client

client = get_client(host = 'localhost' , port = 8123 , username = 'default' , database = 'AdityaDB')

# Delete user
try:
	client.command("""
		ALTER TABLE users
		DELETE WHERE name = 'Eve'
	""")
	print("Deleted user with name 'Eve'.")
except Exception as e:
	print("Deletion failed...." , e)
