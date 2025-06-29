from network.vpc import Vpc
from network.subnet import Subnet
from network.securitygroup import SecurityGroup

vpc_id = "vpc-05567b3334f8c2265"

def network():
    # vpc = Vpc(name="hcs-an2-vpc", cidr_block="10.212.0.0/16")

    # subnet_dev = Subnet("hcs-dev-an2-subnet-a", vpc.id, "10.212.1.0/24", "ap-northeast-2a")
    # subnet_stg = Subnet("hcs-stg-an2-subnet-a", vpc.id, "10.212.10.0/24", "ap-northeast-2a")
    # subnet_prod = Subnet("hcs-prod-an2-subnet-a", vpc.id, "10.212.100.0/24", "ap-northeast-2a")

    # sg_dev = SecurityGroup("hcs-dev-an2-sg", vpc.id)
    # sg_stg = SecurityGroup("hcs-stg-an2-sg", vpc.id)
    # sg_prod = SecurityGroup("hcs-prod-an2-sg", vpc.id)

    # return vpc, subnet_dev, subnet_stg, subnet_prod, sg_dev, sg_stg, sg_prod

    sg_dev = SecurityGroup("hcs-dev-an2-sg", vpc_id)
    sg_stg = SecurityGroup("hcs-stg-an2-sg", vpc_id)
    sg_prod = SecurityGroup("hcs-prod-an2-sg", vpc_id)
    
    return sg_dev, sg_stg, sg_prod