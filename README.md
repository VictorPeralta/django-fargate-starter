# django-fargate-starter

Much of the Terraform code comes from https://testdriven.io/blog/deploying-django-to-ecs-with-terraform/#ecs

## Build and push docker images

- Create a repository in ECR
- aws ecr get-login-password --region us-west-1 | docker login --username AWS --password-stdin 731850255422.dkr.ecr.us-west-1.amazonaws.com
- docker buildx build -t <django_repository> --platform linux/amd64 .
- docker buildx build -t <nginx_repository> --platform linux/amd64 .
- docker push <django_repository>
- docker push <nginx_repository>

## Before deploying

- Create .env.dev file for local environment
- [Create an SSL Certificate in AWS ACM and configure DNS records](https://us-west-1.console.aws.amazon.com/acm/home?region=us-west-1#/certificates/list)
- Fill in correct values in `terraform.tfvars`

## Deploy with Terraform

- `aws sso login`
- `terraform plan`
- Validate everything looks good
- `terraform apply`

## Manual steps after deployment

- [Point domain to ALB in your DNS settings](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/using-domain-names-with-elb.html#dns-associate-custom-elb) ALB Hostname is a terraform output
- Verify domain in your DNS settings with the CNAME records provided by SES. DKIM values are a terraform output

## Update ECS service to use latest image

If you updated your docker image and want to relaunch services with the latest code, you can run:

`aws ecs update-service --cluster da-cluster --service da-celery-service --force-new-deployment`

The ideal flow might be to actually specify an image version in the vars, not use `latest`, so that tasks can be updated via terraform.

## SSH into a fargate task

If you need to SSH into a fargate task, you can use the command:

```
aws ecs execute-command --cluster <cluster_name> \
    --task <task_id> \
    --container <container_name> \
    --interactive \
    --command "/bin/sh"
```

### TODO

- [x] Add S3 to terraform
- [ ] Add Redis to terraform
- [ ] Auto scaling (more info in blog post above)
- [ ] CI Building for docker images

## SSM into containers
