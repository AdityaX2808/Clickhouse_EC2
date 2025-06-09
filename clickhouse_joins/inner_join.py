from clickhouse_connect import get_client

# Establish connection
client = get_client(
    host='localhost',
    port=8123,
    username='default',
    database='AdityaDB'
)

# JOIN query
query = """
    SELECT 
        u.id AS user_id,
        u.name,
        u.age,
        o.order_id,
        o.amount,
        o.order_date
    FROM users u
    INNER JOIN orders o 
    ON u.id = o.user_id
"""

# Run the query
try:
    result = client.query(query)
    print("INNER JOIN Results:")
    for row in result.result_rows:
        print(row)
except Exception as e:
    print("INNER JOIN failed:", e)
