import csv
from clickhouse_connect import get_client

# Connect to ClickHouse
client = get_client(
    host="localhost",
    port=8123,
    username="default",
    database="AdityaDB"
)

# Query all users
query = "SELECT * FROM users"

try:
    result = client.query(query)
    rows = result.result_rows
    headers = result.column_names

    with open("exported_users.csv", mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    print("Exported users to 'exported_users.csv'")
except Exception as e:
    print("Export failed:", e)
