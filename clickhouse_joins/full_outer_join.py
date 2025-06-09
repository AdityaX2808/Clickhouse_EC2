from clickhouse_connect import get_client

client = get_client(
	host = 'localhost',
	port = 8123,
	username = 'default',
	database = 'AdityaDB'
)

# Full Outer Join Simulation
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
    ON u.id = o.user_id

    UNION ALL

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
    WHERE u.id IS NULL
"""

try:
	result = client.query(query).result_rows
	print("Full Outer Join Results: ")
	for row in result:
		print(row)
except Exception as e:
	print("Full Outer Join Failed....")

