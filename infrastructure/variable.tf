variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "cluster_name" {
  type    = string
  default = "finedge-cluster"
}

variable "vpc_id" {
  type    = string
  default = "vpc-123456"
}

variable "subnets" {
  type    = list(string)
  default = ["subnet-abc", "subnet-def"]
}