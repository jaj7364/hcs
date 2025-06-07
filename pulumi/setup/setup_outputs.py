import pulumi

def export(vpc, subnet, sg, s3, role, policy, user):
    subnet_dev, subnet_stg, subnet_prod = subnet
    sg = (sg_dev, sg_stg, sg_prod) = sg
    s3_dev, s3_stg, s3_prod = s3

    pulumi.export("vpc_id", vpc.id)
    pulumi.export("subnet_dev_id", subnet_dev.id)
    pulumi.export("subnet_stg_id", subnet_stg.id)
    pulumi.export("subnet_prod_id", subnet_prod.id)
    pulumi.export("sg_dev_id", sg_dev.id)
    pulumi.export("sg_stg_id", sg_stg.id)
    pulumi.export("sg_prod_id", sg_prod.id)
    pulumi.export("s3_dev", s3_dev.id)
    pulumi.export("s3_stg", s3_stg.id)
    pulumi.export("s3_prod", s3_prod.id)
    pulumi.export("role", role.id)
    pulumi.export("policy", policy.id)
    pulumi.export("user", user.name)
