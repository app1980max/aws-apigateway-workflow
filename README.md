<img width="1024" height="600" alt="image" src="https://github.com/user-attachments/assets/44de25a9-b042-4aa7-8538-e0eeef9cde40" />


## AWS | API Gateway + Lambda  
Serverless ETL pipeline built with AWS Lambda, designed to ingest JSON data (e.g., from Facebook) and store it into a PostgreSQL database hosted in AWS RDS. The entire infrastructure is provisioned using Terraform, including VPC networking, security groups, IAM roles, and Lambda configuration.



🎯 Architecture Overview
```
AWS Lambda: Processes JSON data and writes it to PostgreSQL.
VPC & Subnets: Lambda runs in isolated subnets with proper network access.
Security Group: Controls inbound/outbound access between Lambda and PostgreSQL.
PostgreSQL RDS: Stores the transformed data in a secure, private subnet.
IAM Role: Grants Lambda necessary permissions for CloudWatch logging and VPC ENI creation.
Internet Gateway: Allows Lambda access to external APIs (e.g., Facebook API).
```


🧱 Features
```
✅ Fully automated provisioning with Terraform
✅ High availability using multiple subnets in different Availability Zones
✅ Secure connectivity between Lambda and RDS
✅ Configurable environment variables for database credentials
✅ Easy to extend for other JSON data source
```



🚀 Deployment Options
```
terraform init
terraform validate
terraform plan -var-file="template.tfvars"
terraform apply -var-file="template.tfvars" -auto-approve
```

