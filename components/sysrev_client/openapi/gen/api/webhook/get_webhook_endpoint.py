from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.webhook_endpoint import WebhookEndpoint
from ...types import Response


def _get_kwargs(
    webhook_endpoint_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/webhook_endpoint/{webhook_endpoint_id}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WebhookEndpoint:
    if response.status_code == 200:
        response_200 = WebhookEndpoint.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | WebhookEndpoint]:
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
) -> Response[ErrorResponse | WebhookEndpoint]:
    """Get a webhook endpoint by ID.

    Args:
        webhook_endpoint_id (str):  Example: we_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookEndpoint]
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
) -> ErrorResponse | WebhookEndpoint | None:
    """Get a webhook endpoint by ID.

    Args:
        webhook_endpoint_id (str):  Example: we_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookEndpoint
    """

    return sync_detailed(
        webhook_endpoint_id=webhook_endpoint_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    webhook_endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | WebhookEndpoint]:
    """Get a webhook endpoint by ID.

    Args:
        webhook_endpoint_id (str):  Example: we_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookEndpoint]
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
) -> ErrorResponse | WebhookEndpoint | None:
    """Get a webhook endpoint by ID.

    Args:
        webhook_endpoint_id (str):  Example: we_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookEndpoint
    """

    return (
        await asyncio_detailed(
            webhook_endpoint_id=webhook_endpoint_id,
            client=client,
        )
    ).parsed
