from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.article import Article
from ...models.create_article_input import CreateArticleInput
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateArticleInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/article",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Article | ErrorResponse:
    if response.status_code == 201:
        response_201 = Article.from_dict(response.json())

        return response_201

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Article | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateArticleInput,
) -> Response[Article | ErrorResponse]:
    """Create a new article.

    Args:
        body (CreateArticleInput):  Example: {'source_id': 'src_8293', 'citation': {'title':
            'Hello world', 'type': 'article-journal'}, 'full_texts': [{'file_name':
            'president_16.json', 'content': {'json': {'first_name': 'Abraham', 'last_name':
            'Lincoln'}}}, {'file_name': 'hello_world.pdf', 'content': {'file_data': {'mime_type':
            'application/pdf', 'data': '<B64 string>'}}}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Article | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateArticleInput,
) -> Article | ErrorResponse | None:
    """Create a new article.

    Args:
        body (CreateArticleInput):  Example: {'source_id': 'src_8293', 'citation': {'title':
            'Hello world', 'type': 'article-journal'}, 'full_texts': [{'file_name':
            'president_16.json', 'content': {'json': {'first_name': 'Abraham', 'last_name':
            'Lincoln'}}}, {'file_name': 'hello_world.pdf', 'content': {'file_data': {'mime_type':
            'application/pdf', 'data': '<B64 string>'}}}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Article | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateArticleInput,
) -> Response[Article | ErrorResponse]:
    """Create a new article.

    Args:
        body (CreateArticleInput):  Example: {'source_id': 'src_8293', 'citation': {'title':
            'Hello world', 'type': 'article-journal'}, 'full_texts': [{'file_name':
            'president_16.json', 'content': {'json': {'first_name': 'Abraham', 'last_name':
            'Lincoln'}}}, {'file_name': 'hello_world.pdf', 'content': {'file_data': {'mime_type':
            'application/pdf', 'data': '<B64 string>'}}}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Article | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateArticleInput,
) -> Article | ErrorResponse | None:
    """Create a new article.

    Args:
        body (CreateArticleInput):  Example: {'source_id': 'src_8293', 'citation': {'title':
            'Hello world', 'type': 'article-journal'}, 'full_texts': [{'file_name':
            'president_16.json', 'content': {'json': {'first_name': 'Abraham', 'last_name':
            'Lincoln'}}}, {'file_name': 'hello_world.pdf', 'content': {'file_data': {'mime_type':
            'application/pdf', 'data': '<B64 string>'}}}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Article | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
