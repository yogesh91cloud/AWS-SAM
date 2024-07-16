
cd .\sam-rds-s3\
 ls
 sam build
 sam deploy --guided
 aws configure
echo "demo-sam-rds" > demo-sam-rds.txt   
 aws s3 cp demo-sam-rds.txt s3://demo-sam-rds/
 aws s3 rm .\demo-sam-rds.txt s3://demo-sam-rds/


PS C:\Users\Yogesh\Documents\sam-rds-s3\sam-rds-s3> **sam deploy --guided**

Configuring SAM deploy
======================

        Looking for config file [samconfig.toml] :  Found
        Reading default arguments  :  Success

        Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [sam-rds-s3-stack]: **sam-rds-s3-stack**
        AWS Region [us-east-1]: us-east-1
        #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
        Confirm changes before deploy [Y/n]: y
        #SAM needs permission to be able to create roles to connect to the resources in your template
        Allow SAM CLI IAM role creation [Y/n]: y
        #Preserves the state of previously provisioned resources when an operation fails
        Disable rollback [Y/n]: y
        Save arguments to configuration file [Y/n]: y
        SAM configuration file [samconfig.toml]: samconfig.toml
        SAM configuration environment [default]: default
