import json
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Get the bucket and file from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    # Download the file
    download_path = '/tmp/{}'.format(file_key)
    s3_client.download_file(source_bucket, file_key, download_path)

    # Perform data processing (example: convert text to uppercase)
    with open(download_path, 'r') as file:
        content = file.read()
    processed_content = content.upper()

    # Save processed file to destination bucket
    destination_bucket = 'your-destination-bucket-name'
    processed_file_key = 'processed_' + file_key
    s3_client.put_object(Bucket=destination_bucket, Key=processed_file_key, Body=processed_content)

    return {
        'statusCode': 200,
        'body': json.dumps('File processed successfully')
    }
