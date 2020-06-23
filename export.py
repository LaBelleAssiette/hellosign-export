import os
import csv
from hellosign_sdk import HSClient

# Initialize HSClient using api key
client = HSClient(api_key=os.environ['HELLOSIGN_API_KEY'])

account = client.get_account_info()

print(account)


with open('documents.csv', 'w') as csvfile:
    reader = csv.writer(csvfile, newline='\n')
    reader.writerow([
        'signature_request_id',
        'test_mode',
        'is_complete',
        'title',
        'signed_at',
        'signer_email_address',
        'signer_name',
        'signature_id',
    ])

    page = 1
    signature_request_list = client.get_signature_request_list(page_size=20, page=page)

    while len(signature_request_list):
        print(len(signature_request_list))

        for signature_request in signature_request_list:
            reader.writerow([
                signature_request.signature_request_id,
                signature_request.test_mode,
                signature_request.is_complete,
                signature_request.title,
                signature_request.signatures[0].signed_at,
                signature_request.signatures[0].signer_email_address,
                signature_request.signatures[0].signer_name,
                signature_request.signatures[0].signature_id,
            ])

            # download file
            if signature_request.is_complete:
                print("Downloading {}".format(signature_request.signature_request_id))
                client.get_signature_request_file(
                    signature_request.signature_request_id,
                    filename="files/" + signature_request.signature_request_id + ".pdf"
                )

        page = page + 1
        signature_request_list = client.get_signature_request_list(page_size=20, page=page)
