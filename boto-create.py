# -*- coding: utf-8 -*-
"""
Creates a S3 bucket and displays the access key and secret that
will have access only to the created bucket.


$ export AWS_ACCESS_KEY_ID=<access_key>
$ export AWS_SECRET_ACCESS_KEY=<secret_key>


"""

import json
import re

import boto3



try:
    input = raw_input
except NameError:
    pass


def is_valid_bucket_name(name):
    BUCKET_RE = re.compile(r'^(?![-.])(?!.*[.-]{2})[a-zA-Z0-9.-]{3,63}(?<![.-])$')
    return BUCKET_RE.match(name)


iam_username = bucket_name = input("Enter S3 bucket name: ")
assert is_valid_bucket_name(bucket_name), "Please enter a valid bucket name."

iam = boto3.resource('iam')
user = iam.create_user(UserName=iam_username)

# Create AccessKey/SecretKey pair for User

accesskeypair = user.create_access_key_pair()
print("Access Key: %s" % accesskeypair.id)
print("Access Secret: %s" % accesskeypair.secret)

user_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],

            "Resource": ["arn:aws:s3:::%s/*" % bucket_name,
                         "arn:aws:s3:::%s" % bucket_name
                         ]
        }
    ]

}

iam.create_policy(
    PolicyName=('S3RO%s' % bucket_name),
    PolicyDocument=json.dumps(user_policy)
)


# iam.put_user_policy(iam_username, ('S3RO%s' % bucket_name), user_policy)
# change accout id
iam = boto3.client('iam')

# iam.attach_user_policy(
iam.put_user_policy(
    PolicyDocument=json.dumps(user_policy),
    PolicyName=('S3RO%s' % bucket_name),
    UserName=iam_username
)

print("Created User {username} with arn={arn}".format(username=user.name,
                                                      arn=user.arn))


#
# Now create bucket
s3 = boto3.resource('s3')
bucket = s3.create_bucket(Bucket=bucket_name)

print("Bucket Name: %s" % bucket.name)


def main():
    create_user_role(user_policy)

    if __name__ == "__main__":
        main()
