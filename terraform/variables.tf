variable "region" {
  description = "The AWS region to create resources in."
  default     = "us-west-1"
}



# networking

variable "public_subnet_1_cidr" {
  description = "CIDR Block for Public Subnet 1"
  default     = "10.0.1.0/24"
}
variable "public_subnet_2_cidr" {
  description = "CIDR Block for Public Subnet 2"
  default     = "10.0.2.0/24"
}
variable "private_subnet_1_cidr" {
  description = "CIDR Block for Private Subnet 1"
  default     = "10.0.3.0/24"
}
variable "private_subnet_2_cidr" {
  description = "CIDR Block for Private Subnet 2"
  default     = "10.0.4.0/24"
}
variable "availability_zones" {
  description = "Availability zones"
  type        = list(string)
  default     = ["us-west-1a", "us-west-1c"]
}

# load balancer

variable "health_check_path" {
  description = "Health check path for the default target group"
  default     = "/ping/"
}

# logs

variable "log_retention_in_days" {
  default = 30
}


# ecs

variable "ecs_cluster_name" {
  description = "Name of the ECS cluster"
  default     = "da"
}
variable "amis" {
  description = "Which AMI to spawn."
  default = {
    us-west-1 = "ami-0bd3976c0dbacc605",
  }
}

variable "docker_image_url_django" {
  description = "Docker image to run in the ECS cluster"
}

variable "docker_image_url_nginx" {
  description = "Docker image to run in the ECS cluster"
}

variable "app_count" {
  description = "Number of Docker containers to run"
  default     = 2
}


# auto scaling

variable "autoscale_min" {
  description = "Minimum autoscale (number of EC2)"
  default     = "1"
}
variable "autoscale_max" {
  description = "Maximum autoscale (number of EC2)"
  default     = "10"
}
variable "autoscale_desired" {
  description = "Desired autoscale (number of EC2)"
  default     = "4"
}

# rds

variable "rds_db_name" {
  description = "RDS database name"
  default     = "mydb"
}
variable "rds_username" {
  description = "RDS database username"
  default     = "foo"
}
variable "rds_password" {
  description = "RDS database password"
}
variable "rds_instance_class" {
  description = "RDS instance type"
  default     = "db.t3.micro"
}

# domain

variable "domain" {
  description = "Domain name to verify for AWS SES"
}

variable "certificate_arn" {
  description = "AWS Certificate Manager ARN for validated domain"
}

variable "django_allowed_hosts" {
  description = "Space separated value for Django's ALLOWED_HOSTS"
}

variable "django_csrf_trusted_origins" {
  description = "Space separated value for Django's CSRF_TRUSTED_ORIGINS"
}

variable "ses_smtp_endpoint" {
  description = "Amazon SES SMTP endpoint"
  default     = "email-smtp.us-west-1.amazonaws.com"
}

variable "ses_smtp_port" {
  description = "The SMTP port"
  default     = 587
}

variable "default_from_email" {
  description = "Default email to send from"
}

# S3 bucket
variable "private_bucket_name" {
  description = "private S3 Bucket name"
  default     = "dfs-private"
}
