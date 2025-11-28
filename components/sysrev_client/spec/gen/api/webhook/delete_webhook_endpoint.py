from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_webhook_endpoint_response_200 import DeleteWebhookEndpointResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    webhook_endpoint_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v2/webhook_endpoint/{webhook_endpoint_id}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteWebhookEndpointResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = DeleteWebhookEndpointResponse200.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteWebhookEndpointResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhook_endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteWebhookEndpointResponse200 | ErrorResponse]:
    """Delete a webhook endpoint.

    Args:
        webhook_endpoint_id (str):  Example: we_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWebhookEndpointResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        webhook_endpoint_id=webhook_endpoint_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteWebhookEndpointResponse200 | ErrorResponse | None:
    """Delete a webhook endpoint.

    Args:
        webhook_endpoint_id (str):  Example: we_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWebhookEndpointResponse200 | ErrorResponse
    """

    return sync_detailed(
        webhook_endpoint_id=webhook_endpoint_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    webhook_endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteWebhookEndpointResponse200 | ErrorResponse]:
    """Delete a webhook endpoint.

    Args:
        webhook_endpoint_id (str):  Example: we_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWebhookEndpointResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        webhook_endpoint_id=webhook_endpoint_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteWebhookEndpointResponse200 | ErrorResponse | None:
    """Delete a webhook endpoint.

    Args:
        webhook_endpoint_id (str):  Example: we_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWebhookEndpointResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            webhook_endpoint_id=webhook_endpoint_id,
            client=client,
        )
    ).parsed
