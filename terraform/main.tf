terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
  }
}

provider "local" {}

resource "local_file" "infra_status" {
  filename = "infrastructure.txt"
  content  = <<EOT
File Hash Generator Infrastructure Ready
----------------------------------------
Status: SIMULATED DEPLOYMENT SUCCESS
CI/CD: ACTIVE
DOCKER: ENABLED
EOT
}