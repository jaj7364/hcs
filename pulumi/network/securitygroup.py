import pulumi_aws as aws

class SecurityGroup:
    def __init__(self, name: str, vpc_id):
        self.sg = aws.ec2.SecurityGroup(
            name,
            vpc_id=vpc_id,
            description="Allow all outbound traffic",
            egress=[{
                "protocol": "-1",
                "from_port": 0,
                "to_port": 0,
                "cidr_blocks": ["0.0.0.0/0"],
            }],
            tags={"Name": name}
        )

    @property
    def id(self):
        return self.sg.id

