[
  {
    "name": "celery-beat",
    "image": "${docker_image_url_django}",
    "command": ["celery", "-A", "dango_config", "beat", "-l", "info"],
    "cpu": 256,
    "memory": 512,
    "essential": true,
    "environment": [
      {
        "name": "DJANGO_ALLOWED_HOSTS",
        "value": "${django_allowed_hosts}"
      },
      {
        "name": "DJANGO_CSRF_TRUSTED_ORIGINS",
        "value": "${django_csrf_trusted_origins}"
      },
      {
        "name": "SQL_USER",
        "value": "${rds_username}"
      },
      {
        "name": "SQL_PORT",
        "value": "5432"
      },
      {
        "name": "SECRET_KEY",
        "value": "BERRSECRET123123123"
      },
      {
        "name": "SQL_DATABASE",
        "value": "${rds_db_name}"
      },
      {
        "name": "SQL_PASSWORD",
        "value": "${rds_password}"
      },
      {
        "name": "SQL_HOST",
        "value": "${rds_hostname}"
      },
      {
        "name": "AWS_REGION",
        "value": "${region}"
      },
      {
        "name": "CELERY_BROKER_TRANSPORT",
        "value": "sqs"
      },
      {
        "name": "CELERY_BROKER_URL",
        "value": "sqs://${urlencode(sqs_access_key)}:${urlencode(sqs_secret_key)}@"
      }
    ],
    "mountPoints": [
      {
        "containerPath": "/app/staticfiles",
        "sourceVolume": "static_volume"
      }
    ],
    "volumesFrom": [],
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "/ecs/celery-app",
        "awslogs-region": "${region}",
        "awslogs-stream-prefix": "celery-app-log-stream"
      }
    }
  }
]
