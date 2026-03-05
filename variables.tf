
variable "aws_region" {
  description = "AWS region for deployment"
  type        = string
  default     = "us-west-2"
}

variable "lambda_function_name" {
  default = "serverless-api-handler"
}

variable "api_name" {
  default = "serverless-api"
}

variable "dynamodb_table_name" {
  default = "serverless-data"
}
