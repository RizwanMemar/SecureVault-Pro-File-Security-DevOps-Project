terraform {
  required_providers {
    local = {
      source = "hashicorp/local"
      version = "~> 2.4"
    }
  }
}

provider "local" {}

resource "local_file" "infrastructure" {
  content  = "File Hash Generator Infrastructure Ready"
  filename = "infrastructure.txt"
}