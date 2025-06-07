# __main__.py

import pulumi
from setup import setup_network, setup_s3, setup_account, setup_outputs

# 네트워크 리소스 생성
vpc, \
subnet_dev, subnet_stg, subnet_prod, \
sg_dev, sg_stg, sg_prod \
= setup_network.setup()

# S3 리소스 생성
s3_dev, s3_stg, s3_prod = setup_s3.setup()

# IAM 리소스 생성
role, policy, user = setup_account.setup()

# 결과 출력
setup_outputs.export(
    vpc,
    [subnet_dev, subnet_stg, subnet_prod],
    [sg_dev, sg_stg, sg_prod],
    [s3_dev, s3_stg, s3_prod],
    role, policy, user
)
