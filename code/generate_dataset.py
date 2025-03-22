import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate synthetic transaction data
np.random.seed(42)
num_records = 1000000  # 1 million records
user_ids = np.random.randint(1, 10000, size=num_records)
transaction_amounts = np.random.uniform(10, 5000, size=num_records)
timestamps = [datetime.now() - timedelta(days=np.random.randint(0, 365)) for _ in range(num_records)]
locations = np.random.choice(["New York", "London", "Tokyo", "Paris", "Berlin"], size=num_records)

# Create DataFrame
data = {
    "Transaction_ID": np.arange(1, num_records + 1),
    "User_ID": user_ids,
    "Transaction_Amount": transaction_amounts,
    "Timestamp": timestamps,
    "Location": locations
}
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("../data/sample-dataset.csv", index=False)
print("Dataset generated and saved to data/sample-dataset.csv")