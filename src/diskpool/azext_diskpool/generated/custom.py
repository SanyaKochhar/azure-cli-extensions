# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from azure.cli.core.util import sdk_no_wait


def disk_pool_list(client,
                   resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def disk_pool_show(client,
                   resource_group_name,
                   disk_pool_name):
    return client.get(resource_group_name=resource_group_name,
                      disk_pool_name=disk_pool_name)


def disk_pool_create(client,
                     resource_group_name,
                     disk_pool_name,
                     sku,
                     location,
                     subnet_id,
                     tags=None,
                     availability_zones=None,
                     disks=None,
                     additional_capabilities=None,
                     no_wait=False):
    disk_pool_create_payload = {}
    disk_pool_create_payload['sku'] = sku
    disk_pool_create_payload['tags'] = tags
    disk_pool_create_payload['location'] = location
    disk_pool_create_payload['availability_zones'] = availability_zones
    disk_pool_create_payload['disks'] = disks
    disk_pool_create_payload['subnet_id'] = subnet_id
    disk_pool_create_payload['additional_capabilities'] = additional_capabilities
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       disk_pool_name=disk_pool_name,
                       disk_pool_create_payload=disk_pool_create_payload)


def disk_pool_update(client,
                     resource_group_name,
                     disk_pool_name,
                     tags=None,
                     disks=None,
                     no_wait=False):
    disk_pool_update_payload = {}
    disk_pool_update_payload['tags'] = tags
    disk_pool_update_payload['disks'] = disks
    return sdk_no_wait(no_wait,
                       client.begin_update,
                       resource_group_name=resource_group_name,
                       disk_pool_name=disk_pool_name,
                       disk_pool_update_payload=disk_pool_update_payload)


def disk_pool_delete(client,
                     resource_group_name,
                     disk_pool_name,
                     no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       disk_pool_name=disk_pool_name)


def disk_pool_list_outbound_network_dependency_endpoint(client,
                                                        resource_group_name,
                                                        disk_pool_name):
    return client.list_outbound_network_dependencies_endpoints(resource_group_name=resource_group_name,
                                                               disk_pool_name=disk_pool_name)


def disk_pool_list_skus(client,
                        location):
    return client.list(location=location)


def disk_pool_start(client,
                    resource_group_name,
                    disk_pool_name,
                    no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_start,
                       resource_group_name=resource_group_name,
                       disk_pool_name=disk_pool_name)


def disk_pool_stop(client,
                   resource_group_name,
                   disk_pool_name,
                   no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_deallocate,
                       resource_group_name=resource_group_name,
                       disk_pool_name=disk_pool_name)


def disk_pool_iscsi_target_list(client,
                                resource_group_name,
                                disk_pool_name):
    return client.list_by_disk_pool(resource_group_name=resource_group_name,
                                    disk_pool_name=disk_pool_name)


def disk_pool_iscsi_target_show(client,
                                resource_group_name,
                                disk_pool_name,
                                iscsi_target_name):
    return client.get(resource_group_name=resource_group_name,
                      disk_pool_name=disk_pool_name,
                      iscsi_target_name=iscsi_target_name)


def disk_pool_iscsi_target_create(client,
                                  resource_group_name,
                                  disk_pool_name,
                                  iscsi_target_name,
                                  acl_mode,
                                  target_iqn=None,
                                  static_acls=None,
                                  luns=None,
                                  no_wait=False):
    iscsi_target_create_payload = {}
    iscsi_target_create_payload['acl_mode'] = acl_mode
    iscsi_target_create_payload['target_iqn'] = target_iqn
    iscsi_target_create_payload['static_acls'] = static_acls
    iscsi_target_create_payload['luns'] = luns
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       disk_pool_name=disk_pool_name,
                       iscsi_target_name=iscsi_target_name,
                       iscsi_target_create_payload=iscsi_target_create_payload)


def disk_pool_iscsi_target_update(client,
                                  resource_group_name,
                                  disk_pool_name,
                                  iscsi_target_name,
                                  static_acls=None,
                                  luns=None,
                                  no_wait=False):
    iscsi_target_update_payload = {}
    iscsi_target_update_payload['static_acls'] = static_acls
    iscsi_target_update_payload['luns'] = luns
    return sdk_no_wait(no_wait,
                       client.begin_update,
                       resource_group_name=resource_group_name,
                       disk_pool_name=disk_pool_name,
                       iscsi_target_name=iscsi_target_name,
                       iscsi_target_update_payload=iscsi_target_update_payload)


def disk_pool_iscsi_target_delete(client,
                                  resource_group_name,
                                  disk_pool_name,
                                  iscsi_target_name,
                                  no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       disk_pool_name=disk_pool_name,
                       iscsi_target_name=iscsi_target_name)
