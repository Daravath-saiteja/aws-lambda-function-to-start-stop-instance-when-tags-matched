# AWS lambda-to-start-stop-instances-based-on-tags.

Introduction: We have to start and stop EC2 instances based on tags during working hours to save cost.We are going to automate this by using python code (boto 3) lambda function.

Requirements: 
-->Launch AWS EC2 instanace with tags / Use existing Instance with tags
--> An AWS account with an IAM user to support lambda function
-->Create Lambda Function to start / stop EC2 Instance

# To create lambda function, 
First we need to create IAM role , Always create IAM role with Least privilege access.
Secondly we create Lambda function using the IAM role we create.

#Create new IAM role for our Lambda function.

steps to follow:

Step1 : Go to IAM ,Select policies , create a policy name EC2-start-stop-for-lambda , select option as {}JSON ,

       ################################################################
       #  use the policy code from file in repo and save the policy . #
       ################################################################
       
Step2 : Now go to IAM role  , create a New role name: Role of EC2-instance-start-stop , select AWS services , Select Lambda , on Next now select the IAM policy we have create "EC2-start-stop-for-lambda" and save the role.

step3 : Create Lambda function , Selection Author from scratch , Give function name : Ec2-start-stop-lambda-role" , Runtime = select python 3.9 , select change default execution role option and select use an existing role Here we need to select the IAM Role "EC2-instance-start-stop" which we created in step2 .

       ################################################################
       #  use the Lambda code from file in repo and save the policy . #
       ################################################################











