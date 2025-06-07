from s3.s3 import S3Bucket

def setup():
    s3_dev = S3Bucket("hcs-dev-an2-s3")
    s3_stg = S3Bucket("hcs-stg-an2-s3")
    s3_prod = S3Bucket("hcs-prod-an2-s3")

    return s3_dev, s3_stg, s3_prod