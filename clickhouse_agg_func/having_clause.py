from clickhouse_connect import get_client

# Connect to ClickHouse
client = get_client(
    host='localhost',
    port=8123,
    username='default',
    password='',
    database='AdityaDB'
)

# Group by user and filter using HAVING
query = """
    SELECT 
        user_id, 
        COUNT(*) AS total_orders, 
        SUM(amount) AS total_amount
    FROM orders
    GROUP BY user_id
    HAVING total_amount > 1500
"""

try:
    result = client.query(query)
    print("Users with Total Order Amount > ₹1500:")
    for row in result.result_rows:
        print(f"User ID: {row[0]} | Orders: {row[1]} | Total ₹: {row[2]}")
except Exception as e:
    print("HAVING query failed:", e)
