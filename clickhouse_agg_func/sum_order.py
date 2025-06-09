from clickhouse_connect import get_client

# Connect to ClickHouse
client = get_client(
    host='localhost',
    port=8123,
    username='default',
    password='',
    database='AdityaDB'
)

# SUM of all order amounts
query = "SELECT SUM(amount) AS total_revenue FROM orders"

try:
    result = client.query(query)
    total_revenue = result.result_rows[0][0]
    print(f"Total Revenue from Orders: ₹{total_revenue}")
except Exception as e:
    print("SUM query failed:", e)
