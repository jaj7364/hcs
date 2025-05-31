import pulumi_aws as aws

class Subnet:
    def __init__(self, name: str, vpc_id, cidr_block: str, availability_zone: str):
        self.subnet = aws.ec2.Subnet(
            name,
            vpc_id=vpc_id,
            cidr_block=cidr_block,
            availability_zone=availability_zone,
            map_public_ip_on_launch=False,
            tags={"Name": name}
        )

    @property
    def id(self):
        return self.subnet.id

