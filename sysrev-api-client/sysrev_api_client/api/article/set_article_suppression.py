from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.set_article_suppression_body import SetArticleSuppressionBody
from ...models.set_article_suppression_response_200 import SetArticleSuppressionResponse200
from ...types import Response


def _get_kwargs(
    article_id: str,
    *,
    body: SetArticleSuppressionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v2/article/{article_id}/suppression",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SetArticleSuppressionResponse200:
    if response.status_code == 200:
        response_200 = SetArticleSuppressionResponse200.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | SetArticleSuppressionResponse200]:
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
    body: SetArticleSuppressionBody,
) -> Response[ErrorResponse | SetArticleSuppressionResponse200]:
    """Remove an article from review

    Args:
        article_id (str):  Example: art_1.
        body (SetArticleSuppressionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SetArticleSuppressionResponse200]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    article_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetArticleSuppressionBody,
) -> ErrorResponse | SetArticleSuppressionResponse200 | None:
    """Remove an article from review

    Args:
        article_id (str):  Example: art_1.
        body (SetArticleSuppressionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SetArticleSuppressionResponse200
    """

    return sync_detailed(
        article_id=article_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    article_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetArticleSuppressionBody,
) -> Response[ErrorResponse | SetArticleSuppressionResponse200]:
    """Remove an article from review

    Args:
        article_id (str):  Example: art_1.
        body (SetArticleSuppressionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SetArticleSuppressionResponse200]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    article_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetArticleSuppressionBody,
) -> ErrorResponse | SetArticleSuppressionResponse200 | None:
    """Remove an article from review

    Args:
        article_id (str):  Example: art_1.
        body (SetArticleSuppressionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SetArticleSuppressionResponse200
    """

    return (
        await asyncio_detailed(
            article_id=article_id,
            client=client,
            body=body,
        )
    ).parsed
