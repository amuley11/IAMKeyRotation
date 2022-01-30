import json
import boto3
import os

iam = boto3.client('iam')
secretsmanager = boto3.client('secretsmanager')

def lambda_handler(event, context):
    
    vsecret = os.getenv('secrets')
    secret_list = vsecret.split(';')

    for secret in secret_list:
        get_secret = secretsmanager.get_secret_value(SecretId=secret)
        secret_details = json.loads(get_secret['SecretString'])

        print("For user - " + secret_details['UserName'] + ", inactive Access & Secret keys will be deleted.")
        
        # Extracting the key details from IAM
        key_response = iam.list_access_keys(UserName=secret_details['UserName'])
        
        # Inactive Key Deletion
        for key in key_response['AccessKeyMetadata']:
            if key['Status'] == 'Inactive':
                iam.delete_access_key(AccessKeyId=key['AccessKeyId'],UserName=key['UserName'])
                print("An inactive key - " + key['AccessKeyId'] + ", of " + key['UserName'] + " user has been deleted.")
    
    return "Process of inactive key deletion completed successfully."