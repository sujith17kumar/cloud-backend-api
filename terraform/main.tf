terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "CloudBackendAPI"
      Environment = var.environment
      ManagedBy   = "Terraform"
    }
  }
}

module "vpc" {
  source = "./modules/vpc"

  vpc_cidr             = var.vpc_cidr
  environment          = var.environment
  public_subnet_cidrs  = var.public_subnet_cidrs
  private_subnet_cidrs = var.private_subnet_cidrs
  availability_zones   = var.availability_zones
}

module "security" {
  source = "./modules/security"

  vpc_id      = module.vpc.vpc_id
  environment = var.environment
}

module "compute" {
  source = "./modules/compute"

  environment        = var.environment
  subnet_id          = module.vpc.public_subnet_ids[0]
  security_group_ids = [module.security.web_security_group_id]
  instance_type      = "t3.micro"
  public_key         = try(file("~/.ssh/id_rsa.pub"), "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGdummykeyforciandvalidationscanpurposesOnly=")
}
