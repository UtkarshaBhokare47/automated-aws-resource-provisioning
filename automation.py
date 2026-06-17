import boto3
from datetime import datetime


# AWS Region
region = "ap-south-1"


# ---------------- S3 BUCKET CREATION ----------------

s3 = boto3.client(
    's3',
    region_name=region
)

bucket_name = "boto3-automation-bucket-" + str(datetime.now().timestamp()).replace(".", "")


s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': region
    }
)

print("S3 Bucket Created Successfully")
print("Bucket Name:", bucket_name)



# ---------------- EC2 INSTANCE CREATION ----------------

ec2 = boto3.resource(
    'ec2',
    region_name=region
)


instance = ec2.create_instances(

    ImageId='ami-0e48839c14ca79d52',

    InstanceType='t2.micro',

    MinCount=1,

    MaxCount=1,

    KeyName='aws-project-key',

    SecurityGroupIds=[
        'sg-0ec20e47becebdfb5'
    ]

)


print("EC2 Instance Created Successfully")
print("Instance ID:", instance[0].id)

