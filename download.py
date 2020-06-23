import os
import csv
from hellosign_sdk import HSClient

# Initialize HSClient using api key
client = HSClient(api_key=os.environ['HELLOSIGN_API_KEY'])

account = client.get_account_info()

print(account)

page = 1

with open('documents.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    for row in reader:
        # row variable is a list that represents a row in csv
        print(row)
        print(client.get_signature_request_file(row[0], filename=row[0]))
