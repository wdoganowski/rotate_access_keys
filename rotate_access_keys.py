import sys
import boto3
from datetime import date
import logging

logging.basicConfig(level=logging.WARNING)

def rotate_access_keys(username: str):
    client = boto3.client('iam')
    res = client.list_access_keys(UserName=username)
    accesskeydate = res['AccessKeyMetadata'][0]['CreateDate'].date()
    old_access_key_id = res['AccessKeyMetadata'][0]['AccessKeyId']
    currentdate = date.today()
    active_days = currentdate - accesskeydate
    key_age = int(active_days.days)

    if key_age > 30:
        logging.info("\n\n***************************************************************************************************")
        logging.info("Old Acccess Key ID: "+old_access_key_id+"\n")
        logging.info("Key for user "+username+" is "+str(key_age)+ " days old..Creating new AWS Key")
        create_new_key_response = client.create_access_key(UserName=username)
        new_access_key_id = create_new_key_response['AccessKey']['AccessKeyId']
        new_secret_key = create_new_key_response['AccessKey']['SecretAccessKey']
        logging.info("New Access Key ID: "+new_access_key_id)
        logging.info("New Secret Key: "+new_secret_key)
        logging.info("Deleting the old Access Key...\n")
        logging.info("***************************************************************************************************")
        client.delete_access_key(UserName=username,AccessKeyId=old_access_key_id)
        return new_access_key_id, new_secret_key
    else:
        logging.info("Key for user "+username+" is just "+str(key_age)+" days old..No need to rotate")
        return old_access_key_id, None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <username>")
        sys.exit(1)
    access_key_id, secret_key = rotate_access_keys(sys.argv[1])
    if secret_key:
        print(f"New Access Key ID: {access_key_id}")
        print(f"New Secret Key: {secret_key}")
    else:
        print(f"No new access key created. Keep using Access Key ID: {access_key_id}")