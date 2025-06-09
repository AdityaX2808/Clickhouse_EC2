from clickhouse_connect import get_client

client = get_client(host = 'localhost' , port = 8123 , username = 'default' , database = 'AdityaDB')

# Update User's Age
try:
	client.command("""
ALTER TABLE users
UPDATE age = 35
WHERE name = 'Bob'
""")

	print(" Updated Bob's age to 35.")
except Exception as e:
	print("Update Failed:",e)
