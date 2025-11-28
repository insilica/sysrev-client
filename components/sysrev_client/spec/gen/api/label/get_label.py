from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.label import Label
from ...types import UNSET, Response, Unset


def _get_kwargs(
    label_id: str,
    *,
    quote_schema: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["quote_schema"] = quote_schema

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/label/{label_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | Label:
    if response.status_code == 200:
        response_200 = Label.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | Label]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    label_id: str,
    *,
    client: AuthenticatedClient | Client,
    quote_schema: bool | Unset = UNSET,
) -> Response[ErrorResponse | Label]:
    """Get a label by ID.

    Args:
        label_id (str):  Example: label_1.
        quote_schema (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Label]
    """

    kwargs = _get_kwargs(
        label_id=label_id,
        quote_schema=quote_schema,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    label_id: str,
    *,
    client: AuthenticatedClient | Client,
    quote_schema: bool | Unset = UNSET,
) -> ErrorResponse | Label | None:
    """Get a label by ID.

    Args:
        label_id (str):  Example: label_1.
        quote_schema (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Label
    """

    return sync_detailed(
        label_id=label_id,
        client=client,
        quote_schema=quote_schema,
    ).parsed


async def asyncio_detailed(
    label_id: str,
    *,
    client: AuthenticatedClient | Client,
    quote_schema: bool | Unset = UNSET,
) -> Response[ErrorResponse | Label]:
    """Get a label by ID.

    Args:
        label_id (str):  Example: label_1.
        quote_schema (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Label]
    """

    kwargs = _get_kwargs(
        label_id=label_id,
        quote_schema=quote_schema,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    label_id: str,
    *,
    client: AuthenticatedClient | Client,
    quote_schema: bool | Unset = UNSET,
) -> ErrorResponse | Label | None:
    """Get a label by ID.

    Args:
        label_id (str):  Example: label_1.
        quote_schema (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Label
    """

    return (
        await asyncio_detailed(
            label_id=label_id,
            client=client,
            quote_schema=quote_schema,
        )
    ).parsed
