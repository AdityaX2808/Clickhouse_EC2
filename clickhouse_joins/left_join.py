from clickhouse_connect import get_client

client = get_client(
	host = 'localhost',
	port = 8123,
	username = 'default',
	database = 'AdityaDB'
)

# Left Join
query = """
	SELECT 
		u.id AS user_id,
		u.name,
		u.age,
		o.order_id,
		o.amount,
		o.order_date
	FROM users u
	LEFT JOIN orders o 
	On u.id = o.user_id
"""

try:
	result = client.query(query).result_rows
	print("Left Join Result:")
	for row in result:
		print(row)
except Exception as e:
	print("Left Join Failed.....")
