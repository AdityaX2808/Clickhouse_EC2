from clickhouse_connect import get_client

client = get_client (
	host = 'localhost',
	port = 8123,
	username = 'default',
	database = 'AdityaDB'
)

# Right Join
query = """
	SELECT 
		u.id AS user_id,
        	u.name,
        	u.age,
        	o.order_id,
        	o.amount,
        	o.order_date
	FROM users u
    	RIGHT JOIN orders o 
    	ON u.id = o.user_id
"""

try: 
	result = client.query(query).result_rows
	print("Right Join Result:")
	for row in result:
		print(row)
except Exceptions as e:
	print("Right Join failed.....")

