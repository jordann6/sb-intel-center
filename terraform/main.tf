data "azurerm_client_config" "current" {}

resource "random_string" "suffix" {
  length  = 6
  special = false
  upper   = false
}

resource "azurerm_resource_group" "sb_intel" {
  name     = var.resource_group_name
  location = var.location
}


resource "azurerm_key_vault" "sb_kv" {
  name                = "kv-sb-intel-${random_string.suffix.result}"
  location            = azurerm_resource_group.sb_intel.location
  resource_group_name = azurerm_resource_group.sb_intel.name
  tenant_id           = data.azurerm_client_config.current.tenant_id
  sku_name            = "standard"

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id

    secret_permissions = ["Get", "List", "Set", "Delete", "Purge"]
  }
}


resource "azurerm_cognitive_account" "openai" {
  name                = var.openai_account_name
  location            = azurerm_resource_group.sb_intel.location
  resource_group_name = azurerm_resource_group.sb_intel.name
  kind                = "OpenAI"
  sku_name            = "S0"
  custom_subdomain_name = "sb-scout-${random_string.suffix.result}"
}

resource "azurerm_cognitive_deployment" "gpt" {
  name                 = var.deployment_name
  cognitive_account_id = azurerm_cognitive_account.openai.id
  model {
    format  = "OpenAI"
    name    = var.model_name
    version = var.model_version
  }
  sku {
    name = "GlobalStandard"
    capacity = 50 
  }
}