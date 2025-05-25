import pulumi_aws as aws

class IamRole:
    def __init__(self, name: str, assume_role_policy: str):
        self.role = aws.iam.Role(
            name,
            assume_role_policy=assume_role_policy,
            tags={"Name": name}
        )

    @property
    def id(self):
        return self.role.id

    @property
    def name(self):
        return self.role.name

    @property
    def arn(self):
        return self.role.arn

class IamPolicy:
    def __init__(self, name: str, policy_json: str):
        self.policy = aws.iam.Policy(
            name,
            policy=policy_json,
            tags={"Name": name}
        )

    @property
    def id(self):
        return self.policy.id

    @property
    def name(self):
        return self.policy.name

    @property
    def arn(self):
        return self.policy.arn

