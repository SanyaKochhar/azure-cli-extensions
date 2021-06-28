# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_dnc_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_dnc.vendored_sdks.dnc import DNC
    return get_mgmt_service_client(cli_ctx,
                                   DNC)


def cf_controller(cli_ctx, *_):
    return cf_dnc_cl(cli_ctx).controller


def cf_delegated_network(cli_ctx, *_):
    return cf_dnc_cl(cli_ctx).delegated_network


def cf_orchestrator_instance_service(cli_ctx, *_):
    return cf_dnc_cl(cli_ctx).orchestrator_instance_service


def cf_delegated_subnet_service(cli_ctx, *_):
    return cf_dnc_cl(cli_ctx).delegated_subnet_service
