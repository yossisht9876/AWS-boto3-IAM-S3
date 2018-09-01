# -*- coding: utf-8 -*-
"""
Creates a S3 bucket and displays the access key and secret that
will have access only to the created bucket.


$ export AWS_ACCESS_KEY_ID=<access_key>
$ export AWS_SECRET_ACCESS_KEY=<secret_key>


"""

import re

import boto3

try:
    input = raw_input

except NameError:
    pass


def is_valid_bucket_name(name):
    BUCKET_RE = re.compile(r'^(?![-.])(?!.*[.-]{2})[a-zA-Z0-9.-]{3,63}(?<![.-])$')
    return BUCKET_RE.match(name)


iam_username = bucket_name = input("Enter S3 bucket name for delete: ")
assert is_valid_bucket_name(bucket_name), "Please enter a valid bucket name."


iam = boto3.client('iam')

response = iam.list_user_policies(UserName=bucket_name)
for policy_name in response['PolicyNames']:
    print("deleting inline policy for user: {}: {}".format(bucket_name, policy_name))

    iam.delete_user_policy(UserName=bucket_name, PolicyName=policy_name)

response = iam.list_access_keys(UserName=bucket_name)
for key_id in [metadata['AccessKeyId'] for metadata in response['AccessKeyMetadata']]:
    print("deleting access key for user {}: {}".format(bucket_name, key_id))

    iam.delete_access_key(UserName=bucket_name, AccessKeyId=key_id)

client = boto3.client('iam')
response = client.delete_policy(PolicyArn='arn:aws:iam::xxxxxxxxx:policy/S3RO%s' % bucket_name)

print(response)

client = boto3.client('iam')

response = client.delete_user(UserName=iam_username)

print("deleting user: {}".format(bucket_name))


# Delete Bucket
client = boto3.client('s3')
response = client.delete_bucket(Bucket=bucket_name)
print('%s bucket deleted successfully' % bucket_name)


def main():
    if __name__ == "__main__":
        main()
