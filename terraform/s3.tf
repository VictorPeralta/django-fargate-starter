resource "aws_s3_bucket" "prod_media" {
  bucket = var.private_bucket_name

}

resource "aws_iam_role_policy" "ecs-task-role-s3-policy" {
  name = "ecs_service_role_s3_policy"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:*",
        ]
        Effect = "Allow"
        Resource = [
          "${aws_s3_bucket.prod_media.arn}",
          "${aws_s3_bucket.prod_media.arn}/*"
        ]
      },
    ]
  })
  role = aws_iam_role.ecs-task-role.id
}

