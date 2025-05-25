import pulumi_aws as aws

class Vpc:
    def __init__(self, name: str, cidr_block: str):
        self.vpc = aws.ec2.Vpc(
            name,
            cidr_block=cidr_block,
            enable_dns_hostnames=True,
            enable_dns_support=True,
            tags={"Name": name}
        )

    @property
    def id(self):
        return self.vpc.id

    @property
    def arn(self):
        return self.vpc.arn

