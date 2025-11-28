from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_article_suppression_response_200 import DeleteArticleSuppressionResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    article_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v2/article/{article_id}/suppression",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteArticleSuppressionResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = DeleteArticleSuppressionResponse200.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteArticleSuppressionResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    article_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteArticleSuppressionResponse200 | ErrorResponse]:
    """Remove an article from review

    Args:
        article_id (str):  Example: art_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteArticleSuppressionResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    article_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteArticleSuppressionResponse200 | ErrorResponse | None:
    """Remove an article from review

    Args:
        article_id (str):  Example: art_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteArticleSuppressionResponse200 | ErrorResponse
    """

    return sync_detailed(
        article_id=article_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    article_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteArticleSuppressionResponse200 | ErrorResponse]:
    """Remove an article from review

    Args:
        article_id (str):  Example: art_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteArticleSuppressionResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    article_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteArticleSuppressionResponse200 | ErrorResponse | None:
    """Remove an article from review

    Args:
        article_id (str):  Example: art_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteArticleSuppressionResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            article_id=article_id,
            client=client,
        )
    ).parsed
