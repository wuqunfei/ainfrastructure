"""An Azure RM Python Pulumi program"""
import pulumi
import pulumi_azure as azure

current = azure.core.get_client_config()
example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
example_insights = azure.appinsights.Insights("exampleInsights",
                                              location=example_resource_group.location,
                                              resource_group_name=example_resource_group.name,
                                              application_type="web")

example_key_vault = azure.keyvault.KeyVault("exampleKeyVault",
                                            location=example_resource_group.location,
                                            resource_group_name=example_resource_group.name,
                                            tenant_id=current.tenant_id,
                                            sku_name="premium")

example_account = azure.storage.Account("exampleaccount",
                                        location=example_resource_group.location,
                                        resource_group_name=example_resource_group.name,
                                        account_tier="Standard",
                                        account_replication_type="GRS")

example_workspace = azure.machinelearning.Workspace("exampleWorkspace",
                                                    location=example_resource_group.location,
                                                    resource_group_name=example_resource_group.name,
                                                    application_insights_id=example_insights.id,
                                                    key_vault_id=example_key_vault.id,
                                                    storage_account_id=example_account.id,
                                                    identity=azure.machinelearning.WorkspaceIdentityArgs(
                                                        type="SystemAssigned",
                                                    ))
