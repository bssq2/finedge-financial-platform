output "eks_cluster_name" {
  description = "EKS cluster name"
  value       = module.eks.cluster_id
}

output "eks_cluster_endpoint" {
  description = "Kubernetes API server endpoint"
  value       = module.eks.cluster_endpoint
}