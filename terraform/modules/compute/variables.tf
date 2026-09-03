variable "environment" {
  type = string
}

variable "subnet_id" {
  type        = string
  description = "Public subnet ID for the instance"
}

variable "security_group_ids" {
  type        = list(string)
  description = "List of security group IDs to attach"
}

variable "instance_type" {
  type    = string
  default = "t2.micro"
}
