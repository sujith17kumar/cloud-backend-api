# Cloud Backend API — Production Infrastructure & GitOps CI/CD

An end-to-end, production-grade cloud deployment featuring a containerized Python backend deployed onto AWS using modular Terraform (IaC) and automated GitHub Actions CI/CD pipelines.

## Architecture Overview
[ Developer Push / PR ]
│
▼
[ GitHub Actions CI ]
├── 1. Terraform fmt & validate
├── 2. Trivy IaC Security Scan
├── 3. Multi-stage Docker Build (Buildx + Cache)
└── 4. Trivy Container Vulnerability Scan
│
▼
[ GitHub Packages (GHCR) ] ── (Image Registry)
│
▼
[ GitHub Actions CD ]
└── SSH Deployment Runner
│
▼
[ AWS Cloud (ap-south-1) ]
└── Custom VPC (10.0.0.0/16)
├── Public Subnets & Internet Gateway
├── Security Group (Least Privilege: 8000/8080, 22)
└── EC2 Instance (t3.micro, Ubuntu 22.04 LTS)
└── Docker Engine Runtime ──> backend-api (v2.1.0)

## Tech Stack & Tooling

* **Cloud Infrastructure:** AWS (EC2, VPC, Internet Gateway, Subnets, Route Tables, Security Groups)
* **Infrastructure as Code:** Terraform (Modular architecture, remote-ready state design)
* **Container Runtime:** Docker Engine, Multi-stage builds, Distroless/Slim patterns
* **CI/CD Automation:** GitHub Actions (IaC linting, Trivy static analysis, GHCR publishing, SSH CD)
* **Application:** Python HTTP API (`/health` monitoring endpoints)
* **Security & Compliance:** Trivy (IaC misconfiguration checks & container CVE scanning)

## Infrastructure Topology (Terraform)

The infrastructure is broken down into reusable Terraform modules:

* `modules/vpc`: Creates isolated virtual private network with public subnets and IGW routing.
* `modules/security`: Manages inbound/outbound firewall rules with granular port binding.
* `modules/compute`: Deploys compute instances with automated Docker bootstrapping via `cloud-init`.

### Provisioning Commands

```bash
cd terraform
terraform init
terraform fmt -check
terraform validate
terraform apply -auto-approve
