# File: infrastructure/main.tf
# ----------------------------

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      # Compatible with terraform‑aws‑eks v20.x
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
  version = "20.36.0"

  # ─────────────────────────────────────────
  # Mandatory inputs
  # ─────────────────────────────────────────
  cluster_name    = var.cluster_name
  cluster_version = "1.23"
  vpc_id          = var.vpc_id

  # CHANGED: `subnets` ➞ `subnet_ids`
  subnet_ids      = var.subnets

  # Optional features
  enable_irsa = true
}

output "cluster_name" {
  value = module.eks.cluster_id
}

output "cluster_endpoint" {
  value = module.eks.cluster_endpoint
}