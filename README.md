
cd .\sam-rds-s3\
 ls
 sam build
 sam deploy --guided
 aws configure
echo "demo-sam-rds" > demo-sam-rds.txt   
 aws s3 cp demo-sam-rds.txt s3://demo-sam-rds/
 aws s3 rm .\demo-sam-rds.txt s3://demo-sam-rds/

