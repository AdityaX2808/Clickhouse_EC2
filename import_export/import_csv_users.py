import csv
from clickhouse_connect import get_client

# Connect to ClickHouse
client = get_client(
    host="localhost",
    port=8123,
    username="default",
    password="",
    database="AdityaDB"
)

# Path to CSV file
csv_file = "exported_users.csv"

# Read CSV and prepare data
try:
    with open(csv_file, mode="r") as f:
        reader = csv.reader(f)
        headers = next(reader)  # First row is header
        data = [tuple(row) for row in reader]

    # Insert data into users table
    client.insert(
        table="user",
        data=data,
        column_names=headers
    )

    print(f"Imported data from '{csv_file}' into 'users' table")
except Exception as e:
    print("Import failed:", e)
