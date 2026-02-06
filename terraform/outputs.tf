output "openai_endpoint" {
  value = azurerm_cognitive_account.openai.endpoint
}

output "openai_primary_key" {
  value     = azurerm_cognitive_account.openai.primary_access_key
  sensitive = true
}

output "key_vault_uri" {
  value = azurerm_key_vault.sb_kv.vault_uri
}

output "resource_group_name" {
  value = azurerm_resource_group.sb_intel.name
}