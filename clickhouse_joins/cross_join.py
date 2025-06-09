from clickhouse_connect import get_client

client = get_client(
	host = 'localhost',
	port = 8123,
	username = 'default',
	database = 'AdityaDB'
)

# Cross Join
query = """
    SELECT 
        u.id AS user_id,
        u.name,
        o.order_id,
        o.amount
    FROM users u
    CROSS JOIN orders o
"""

try: 
	result = client.query(query).result_rows
	print("Cross Join Result: (Cartesian Product)")
	for row in result:
		print(row)
except Exception as e:
	print("Cross Join Failed.....")
