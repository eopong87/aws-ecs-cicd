# AWS ECS Fargate with Docker and CI/CD

A containerized Flask application deployed to AWS ECS Fargate with an automated CI/CD pipeline using GitHub Actions, provisioned with Terraform.

## What I Built
- Flask web application containerized with Docker
- ECR repository for storing Docker images
- ECS Fargate cluster running 2 containers
- Application Load Balancer for traffic distribution
- GitHub Actions pipeline for automated deployments
- VPC with public subnets across 2 Availability Zones

## Services Used
- **Docker** - containerization
- **AWS ECR** - Docker image registry
- **AWS ECS Fargate** - serverless container orchestration
- **AWS ALB** - load balancing
- **GitHub Actions** - CI/CD pipeline
- **Terraform** - infrastructure as code

## How It Works
1. Push code to GitHub main branch
2. GitHub Actions automatically triggers
3. Builds new Docker image
4. Pushes image to ECR with git SHA tag
5. Updates ECS task definition
6. Deploys to ECS Fargate
7. Live site updates automatically

## How to Deploy
1. Clone this repo
2. Configure AWS CLI with `aws configure`
3. Add AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY as GitHub Secrets
4. Navigate to terraform folder
5. Run `terraform init`
6. Run `terraform apply`
7. Push your Docker image to ECR
8. Push any code change to trigger the pipeline

## What I Learned
- How to containerize applications with Docker
- How ECR stores and manages Docker images
- How ECS Fargate runs containers without managing servers
- How GitHub Actions automates build and deploy pipelines
- How to use git SHA for image versioning
- End to end CI/CD workflow
