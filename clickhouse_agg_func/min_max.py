from clickhouse_connect import get_client

# Connect to ClickHouse
client = get_client(
    host='localhost',
    port=8123,
    username='default',
    password='',
    database='AdityaDB'
)

# MIN and MAX order amounts
query = """
    SELECT 
        MIN(amount) AS min_order_amount,
        MAX(amount) AS max_order_amount
    FROM orders
"""

try:
    result = client.query(query)
    min_amount, max_amount = result.result_rows[0]
    print(f"Minimum Order Amount: ₹{min_amount}")
    print(f"Maximum Order Amount: ₹{max_amount}")
except Exception as e:
    print("MIN/MAX query failed:", e)
