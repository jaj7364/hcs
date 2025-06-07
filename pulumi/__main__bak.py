import pulumi
from network import Vpc, Subnet, SecurityGroup
from s3 import S3Bucket
from account import IamRole, IamPolicy, IamUser

# VPC 생성
vpc = Vpc(name="hcs-an2-vpc", cidr_block="10.212.0.0/16")

# Subnet 생성 (서울 리전 AZ)
subnet_dev = Subnet(
    name="hcs-dev-an2-subnet-a",
    vpc_id=vpc.id,
    cidr_block="10.212.10.0/24",
    availability_zone="ap-northeast-2a"
)

subnet_stg = Subnet(
    name="hcs-stg-an2-subnet-a",
    vpc_id=vpc.id,
    cidr_block="10.212.20.0/24",
    availability_zone="ap-northeast-2a"
)

subnet_prod = Subnet(
    name="hcs-prod-an2-subnet-a",
    vpc_id=vpc.id,
    cidr_block="10.212.30.0/24",
    availability_zone="ap-northeast-2a"
)

# Security Group 생성
sg_dev = SecurityGroup(name="hcs-dev-an2-sg", vpc_id=vpc.id)
sg_stg = SecurityGroup(name="hcs-stg-an2-sg", vpc_id=vpc.id)
sg_prod = SecurityGroup(name="prod-an2-sg", vpc_id=vpc.id)

#S3 생성
bucket_dev = S3Bucket("hcs-dev-an2-s3")
bucket_stg = S3Bucket("hcs-stg-an2-s3")
bucket_prod = S3Bucket("hcs-prod-an2-s3")

#IAM Role 생성
role = IamRole(
    name="hcs-an2-role-sts",
    assume_role_policy="""{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Service": "ec2.amazonaws.com"
          },
          "Action": "sts:AssumeRole"
        }
      ]
    }"""
)

#IAM Policy 생성
policy = IamPolicy(
    name="hcs-an2-policy-s3",
    policy_json="""{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": "s3:GetObject",
          "Resource": "*"
        }
      ]
    }"""
)

#IAM USER 생성
user = IamUser("hcs-an2-user-cli")

# 출력
pulumi.export("vpc_id", vpc.id)
pulumi.export("subnet_dev_id", subnet_dev.id)
pulumi.export("subnet_stg_id", subnet_stg.id)
pulumi.export("subnet_prod_id", subnet_prod.id)
pulumi.export("sg_dev_id", sg_dev.id)
pulumi.export("sg_stg_id", sg_stg.id)
pulumi.export("sg_prod_id", sg_prod.id)
pulumi.export("bucket_dev", bucket_dev.id)
pulumi.export("bucket_stg", bucket_stg.id)
pulumi.export("bucket_prod", bucket_prod.id)
pulumi.export("role", role.id)
pulumi.export("policy", policy.id)
pulumi.export("user", user.name)
