import pulumi_aws as aws

class S3Bucket:
    def __init__(self, name: str):
        self.bucket = aws.s3.Bucket(
            resource_name=name,
            acl="private",
            tags={"Name": name}
        )

    @property
    def id(self):
        return self.bucket.id

    @property
    def bucket_domain_name(self):
        return self.bucket.bucket_domain_name

