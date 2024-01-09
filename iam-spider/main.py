from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.authorization import AuthorizationManagementClient

def get_users(graph_client, tenant_id):
    """
    Get a list of users in the Azure AD.

    :param graph_client: Azure Graph client
    :param tenant_id: Azure AD tenant ID
    :return: List of user objects
    """
    users = graph_client.users.list(filter=f"extension_{tenant_id}_IsAppOwner eq false")
    return list(users)

def get_user_permissions(authz_client, principal_id, scope):
    """
    Get the permissions attached to a specific user.

    :param authz_client: Azure Authorization client
    :param principal_id: User's principal ID
    :param scope: The scope for which permissions need to be retrieved
    :return: List of permissions
    """
    permissions = authz_client.permissions.list(principal_id=principal_id, resource_group_name=scope['resource_group'], resource_provider_name=scope['resource_provider'], resource_type=scope['resource_type'], resource_name=scope['resource_name'])
    return list(permissions)

def spiderweb_azure(graph_client, authz_client, tenant_id):
    """
    Spiderweb through Azure AD users, get their permissions, and perform auditing.

    :param graph_client: Azure Graph client
    :param authz_client: Azure Authorization client
    :param tenant_id: Azure AD tenant ID
    """
    users = get_users(graph_client, tenant_id)

    for user in users:
        user_principal_id = user.object_id
        user_display_name = user.display_name
        print(f"\nAnalyzing permissions for user: {user_display_name}")

        # Replace the scope with your specific resource details
        scope = {
            'resource_group': 'your_resource_group',
            'resource_provider': 'Microsoft.YourResourceProvider',
            'resource_type': 'your_resource_type',
            'resource_name': 'your_resource_name'
        }

        user_permissions = get_user_permissions(authz_client, user_principal_id, scope)
        
        # Map permissions to numerical values
        permission_values = map_permissions_to_values(user_permissions)
        
def map_permissions_to_values(permissions):
    """
    Map Azure permissions to numerical values ranging from 1-1000 ascending based on level of privilege.
    Global admins are capped at 1000.

    :param permissions: List of permissions
    :return: Dictionary mapping permissions to numerical values
    """
    permission_values = {}
    sorted_permissions = sorted(permissions, key=lambda x: x.actions)
    num_permissions = len(sorted_permissions)
    for i, permission in enumerate(sorted_permissions):
        if permission.actions == 'Microsoft.Authorization/*/Write':
            permission_values[permission.actions] = 1000
        else:
            permission_values[permission.actions] = (i + 1) * (1000 // num_permissions)
    return permission_values
    main()

def main():
    # Initialize Azure clients
    credential = DefaultAzureCredential()
    graph_client = GraphRbacManagementClient(credential, 'your_tenant_id')
    authz_client = AuthorizationManagementClient(credential, 'your_subscription_id')

    # Call the spiderweb function
    spiderweb_azure(graph_client, authz_client, 'your_tenant_id')

if __name__ == "__main__":
    main()
