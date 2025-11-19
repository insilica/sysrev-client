from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.new_label_body import NewLabelBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: NewLabelBody,
    project_id: str | Unset = UNSET,
    quote_schema: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["project_id"] = project_id

    params["quote_schema"] = quote_schema

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/label",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse:
    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewLabelBody,
    project_id: str | Unset = UNSET,
    quote_schema: bool | Unset = UNSET,
) -> Response[ErrorResponse]:
    """Create a new label.

    Args:
        project_id (str | Unset):  Example: proj_125327.
        quote_schema (bool | Unset):
        body (NewLabelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        project_id=project_id,
        quote_schema=quote_schema,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: NewLabelBody,
    project_id: str | Unset = UNSET,
    quote_schema: bool | Unset = UNSET,
) -> ErrorResponse | None:
    """Create a new label.

    Args:
        project_id (str | Unset):  Example: proj_125327.
        quote_schema (bool | Unset):
        body (NewLabelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        project_id=project_id,
        quote_schema=quote_schema,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewLabelBody,
    project_id: str | Unset = UNSET,
    quote_schema: bool | Unset = UNSET,
) -> Response[ErrorResponse]:
    """Create a new label.

    Args:
        project_id (str | Unset):  Example: proj_125327.
        quote_schema (bool | Unset):
        body (NewLabelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        project_id=project_id,
        quote_schema=quote_schema,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewLabelBody,
    project_id: str | Unset = UNSET,
    quote_schema: bool | Unset = UNSET,
) -> ErrorResponse | None:
    """Create a new label.

    Args:
        project_id (str | Unset):  Example: proj_125327.
        quote_schema (bool | Unset):
        body (NewLabelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            project_id=project_id,
            quote_schema=quote_schema,
        )
    ).parsed
