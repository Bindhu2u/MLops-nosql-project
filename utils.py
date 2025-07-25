# utils.py
from config import collection

# Insert sample customer data
collection.insert_many([
    {
        "customer_id": "C001",
        "age": 30,
        "tenure": 3,
        "services": ["Internet", "Phone"],
        "monthly_charge": 65.0
    },
    {
        "customer_id": "C002",
        "age": 45,
        "tenure": 6,
        "services": ["Internet", "Phone"],
        "monthly_charge": 55.0
    }
])

print("Sample data inserted successfully.")