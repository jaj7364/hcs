from account.iam import IamRole, IamPolicy, IamUser

def setup():
    role = IamRole(
    name="hcs-an2-role-ec2",
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

    policy = IamPolicy(
    name="hcs-an2-policy-s3",
    policy_json="""{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
          "s3:GetObject",
          "s3:PutObject"
          ],
          "Resource": "*"
        }
      ]
    }"""
    )

    user = IamUser("hcs-an2-user-cli")

    return role, policy, user