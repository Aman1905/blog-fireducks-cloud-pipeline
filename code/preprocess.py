# -------------------------------------------- If the dataset is stored locally -------------------------------------------- 

import fireducks as fd

# Load dataset locally
df_fireducks = fd.read_csv("../data/sample-dataset.csv")

# Preprocessing steps
df_fireducks = df_fireducks.fillna(0)  # Handle missing values
filtered_df = df_fireducks[df_fireducks["Transaction_Amount"] > 1000]  # Filter anomalies
aggregated_df = df_fireducks.groupby("User_ID")["Transaction_Amount"].sum()  # Aggregate user behavior

# Display results
print(aggregated_df)

# -------------------------------------------- If the dataset is stored in AWS S3 -------------------------------------------- 

# import boto3
# import fireducks as fd

# # Configure AWS S3 client
# s3_client = boto3.client(
#     's3',
#     aws_access_key_id="YOUR_ACCESS_KEY",
#     aws_secret_access_key="YOUR_SECRET_KEY"
# )
# bucket_name = "YOUR_BUCKET_NAME"
# file_key = "sample-dataset.csv"

# # Download file from S3
# s3_client.download_file(bucket_name, file_key, "sample-dataset.csv")

# # Load dataset using FireDucks
# df_fireducks = fd.read_csv("sample-dataset.csv")

# # Preprocessing steps
# df_fireducks = df_fireducks.fillna(0)  # Handle missing values
# filtered_df = df_fireducks[df_fireducks["Transaction_Amount"] > 1000]  # Filter anomalies
# aggregated_df = df_fireducks.groupby("User_ID")["Transaction_Amount"].sum()  # Aggregate user behavior

# # Display results
# print(aggregated_df)