from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.project_export import ProjectExport
from ...types import Response


def _get_kwargs(
    project_id: str,
    project_export_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/project/{project_id}/export/{project_export_id}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | ProjectExport:
    if response.status_code == 200:
        response_200 = ProjectExport.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ProjectExport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    project_export_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | ProjectExport]:
    """Get a project export by ID.

    Args:
        project_id (str):  Example: proj_125327.
        project_export_id (str):  Example: project_export_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ProjectExport]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        project_export_id=project_export_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    project_export_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | ProjectExport | None:
    """Get a project export by ID.

    Args:
        project_id (str):  Example: proj_125327.
        project_export_id (str):  Example: project_export_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ProjectExport
    """

    return sync_detailed(
        project_id=project_id,
        project_export_id=project_export_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    project_export_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | ProjectExport]:
    """Get a project export by ID.

    Args:
        project_id (str):  Example: proj_125327.
        project_export_id (str):  Example: project_export_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ProjectExport]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        project_export_id=project_export_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    project_export_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | ProjectExport | None:
    """Get a project export by ID.

    Args:
        project_id (str):  Example: proj_125327.
        project_export_id (str):  Example: project_export_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ProjectExport
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            project_export_id=project_export_id,
            client=client,
        )
    ).parsed
