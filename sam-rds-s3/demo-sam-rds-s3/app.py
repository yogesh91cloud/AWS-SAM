import boto3
import os

rds_client = boto3.client('rds')
s3_bucket = os.getenv('S3_BUCKET')
rds_instance_id = os.getenv('RDS_INSTANCE_ID')
rds_db_name = os.getenv('RDS_DB_NAME')
rds_username = os.getenv('RDS_USERNAME')
rds_password = os.getenv('RDS_PASSWORD')
rds_vpc_security_groups = os.getenv('RDS_VPC_SECURITY_GROUPS').split(',')

def lambda_handler(event, context):
    event_name = event['Records'][0]['eventName']
    if event_name.startswith('ObjectCreated'):
        create_rds_instance()
    elif event_name.startswith('ObjectRemoved'):
        delete_rds_instance()

def create_rds_instance():
    try:
        response = rds_client.create_db_instance(
            DBInstanceIdentifier=rds_instance_id,
            AllocatedStorage=20,
            DBName=rds_db_name,
            Engine='mysql',
            MasterUsername=rds_username,
            MasterUserPassword=rds_password,
            VpcSecurityGroupIds=rds_vpc_security_groups,
            DBInstanceClass='db.t3.micro',
            StorageType='gp2'    
        )
        print(f"Creating RDS Instance: {response}")
    except rds_client.exceptions.DBInstanceAlreadyExistsFault:
        print(f"RDS instance {rds_instance_id} already exists.")

def delete_rds_instance():
    try:
        response = rds_client.delete_db_instance(
            DBInstanceIdentifier=rds_instance_id,
            SkipFinalSnapshot=True
        )
        print(f"Deleting RDS Instance: {response}")
    except rds_client.exceptions.DBInstanceNotFoundFault:
        print(f"RDS instance {rds_instance_id} not found. Nothing to delete.")
