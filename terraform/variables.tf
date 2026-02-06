variable "resource_group_name" {
  type    = string
  default = "rg-superbowl-intel-2026"
}

variable "location" {
  type    = string
  default = "East US"
}

variable "openai_account_name" {
  type    = string
  default = "ai-sb-scout-2026"
}

variable "deployment_name" {
  type    = string
  default = "sb-scout-engine"
}

variable "model_name" {
  type    = string
  default = "gpt-4o" 
}

variable "model_version" {
  type    = string
  default = "2024-11-20" 
}