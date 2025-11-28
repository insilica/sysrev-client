from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.user_billing_usage import UserBillingUsage
from ...types import Response


def _get_kwargs(
    enterprise_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/enterprise/{enterprise_id}/billing/usage",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | UserBillingUsage:
    if response.status_code == 200:
        response_200 = UserBillingUsage.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | UserBillingUsage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    enterprise_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | UserBillingUsage]:
    """Get the allowance and credit balance of an enterprise.

    Args:
        enterprise_id (str):  Example: ent_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UserBillingUsage]
    """

    kwargs = _get_kwargs(
        enterprise_id=enterprise_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    enterprise_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | UserBillingUsage | None:
    """Get the allowance and credit balance of an enterprise.

    Args:
        enterprise_id (str):  Example: ent_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UserBillingUsage
    """

    return sync_detailed(
        enterprise_id=enterprise_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    enterprise_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | UserBillingUsage]:
    """Get the allowance and credit balance of an enterprise.

    Args:
        enterprise_id (str):  Example: ent_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UserBillingUsage]
    """

    kwargs = _get_kwargs(
        enterprise_id=enterprise_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    enterprise_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | UserBillingUsage | None:
    """Get the allowance and credit balance of an enterprise.

    Args:
        enterprise_id (str):  Example: ent_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UserBillingUsage
    """

    return (
        await asyncio_detailed(
            enterprise_id=enterprise_id,
            client=client,
        )
    ).parsed
