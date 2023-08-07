from pulumi_aws import ec2
#from iam.iam import Iam
from vpc.vpc import Vpc
from ec2.ec2 import Ec2


vpc = Vpc()
vpc_id, sg_id, subnet_public_id  = vpc.create()
print(f'ID VPC: {[vpc_id]} - SG:{[sg_id]} - Subnet:{[subnet_public_id]}')
ec2 = Ec2()
ec2_id =ec2.create(vpc_id, sg_id, subnet_public_id)
print(f'DNS: {[ec2_id]}') 

# iam = Iam()
# iam_create_id = iam.create()
# print(f'ID IAM: {iam_create_id}')



