# NOTE: Set AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_REGION as environment variables before running this script.
import boto3
import time
import random
from datetime import datetime
import os

# AWS Kinesis Firehose config
kinesis = boto3.client(
    'firehose',
    region_name=os.getenv('AWS_REGION', 'ap-south-1'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

# Simulated inventory
items = ["Headphones", "Keyboard", "Mouse", "Phone", "Charger"]

# CSV Header
csv_header = "order_id,store_id,item,quantity,price,total_amount,timestamp\n"

# Send header only once
kinesis.put_record(
    DeliveryStreamName="retail-firehose",
    Record={"Data": csv_header}
)

# Function to generate a single CSV row
def generate_order_csv(order_no):
    item = random.choice(items)
    price = round(random.uniform(100, 1500), 2)
    quantity = random.randint(1, 5)
    row = f"ORD{datetime.now().strftime('%Y%m%d')}{str(order_no).zfill(4)}," \
          f"{random.choice(['store_101', 'store_102', 'store_103'])}," \
          f"{item},{quantity},{price},{round(quantity * price, 2)}," \
          f"{datetime.now().strftime('%m/%d/%Y %H:%M')}\n"
    return row

# Send 10 records as CSV
for i in range(1, 11):
    csv_record = generate_order_csv(i)
    kinesis.put_record(
        DeliveryStreamName="retail-firehose",
        Record={"Data": csv_record}
    )
    print(f"[✓] Sent to Firehose (CSV): {csv_record.strip()}")
    time.sleep(2)
