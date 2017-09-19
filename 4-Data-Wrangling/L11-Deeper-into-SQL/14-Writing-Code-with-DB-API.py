import sqlite3

# Connect to database. Cookies is name of database
# Returns connection object that's good until connection closed
conn = sqlite3.connect("Cookies")
# cursor is what runs queries and fetches results
cursor = conn.cursor()
# Execute a query using the cursor
cursor.execute("select host_key from cookies limit 10")
# Fetch results using cursor
results = cursor.fetchall()
print results
# Connection closed
conn.close()
