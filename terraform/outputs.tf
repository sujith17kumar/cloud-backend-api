output "vpc_id" {
  description = "The ID of the custom VPC"
  value       = module.vpc.vpc_id
}

output "public_subnet_ids" {
  description = "IDs of the public subnets"
  value       = module.vpc.public_subnet_ids
}

output "private_subnet_ids" {
  description = "IDs of the private subnets"
  value       = module.vpc.private_subnet_ids
}

output "web_security_group_id" {
  description = "Security Group ID for web traffic"
  value       = module.security.web_security_group_id
}

output "app_server_public_ip" {
  description = "Public IP of the deployed EC2 compute node"
  value       = module.compute.instance_public_ip
}
