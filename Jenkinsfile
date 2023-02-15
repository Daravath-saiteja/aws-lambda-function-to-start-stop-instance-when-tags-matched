pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
        TF_WORKING_DIR = "/var/lib/jenkins/workspace/Aws-lambda-function-to-start-stop-instance-when-tags-matched"
    }

    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', credentialsId: 'e8da9276-cad8-490e-841b-1141af1e508f', url: 'https://github.com/saiteja-18/Aws-lambda-function-to-start-stop-instance-when-tags-matched.git'
            }
        }
        
        stage('Initialize Terraform') {
            steps {
                sh 'terraform init ${TF_WORKING_DIR}'
            }
        }
        
        stage('Validate Terraform') {
            steps {
                sh 'terraform validate ${TF_WORKING_DIR}'
            }
        }
        
        stage('Plan Terraform') {
            steps {
                sh 'terraform plan -out=myplan ${TF_WORKING_DIR}'
            }
        }
        
        stage('Apply Terraform') {
            steps {
                sh 'terraform apply myplan'
            }
        }
        

    }
}
