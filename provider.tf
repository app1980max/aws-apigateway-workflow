
provider "aws" {
  region = "us-west-2"
}

# --- DATA: availability zones ---
data "aws_availability_zones" "available" {}
