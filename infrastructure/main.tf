# File: infrastructure/main.tf
# ----------------------------

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      # UPDATED: the EKS module ≥ 20.x now expects AWS provider ≥ 5.95
      version = "~> 5.0"
    }
  }
  required_version = ">= 1.0"
}

provider "aws" {
  region = var.aws_region
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "20.36.0"          # pin the module version explicitly
  # ───────────────────────────
  cluster_name    = var.cluster_name
  cluster_version = "1.23"
  vpc_id          = var.vpc_id
  subnets         = var.subnets
  enable_irsa     = true
}