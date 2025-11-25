#!/usr/bin/env python

import base64
import os
from pathlib import Path

import pytest

from sysrev_client.openapi.gen.api.article import create_article
from sysrev_client.openapi.gen.api.source import create_source
from sysrev_client.openapi.gen.client import AuthenticatedClient
from sysrev_client.openapi.gen.models.article_full_text import ArticleFullText
from sysrev_client.openapi.gen.models.article_full_text_content_blob import (
    ArticleFullTextContentBlob,
)
from sysrev_client.openapi.gen.models.article_full_text_content_json import (
    ArticleFullTextContentJson,
)
from sysrev_client.openapi.gen.models.blob import Blob
from sysrev_client.openapi.gen.models.create_article_input import CreateArticleInput
from sysrev_client.openapi.gen.models.create_article_input_citation import (
    CreateArticleInputCitation,
)
from sysrev_client.openapi.gen.models.create_source_input import CreateSourceInput


@pytest.fixture(scope="module")
def api_key() -> str:
    api_key = os.getenv("SYSREV_API_KEY")
    if not api_key:
        pytest.skip("SYSREV_API_KEY environment variable not set")
    return api_key


@pytest.fixture(scope="module")
def api_url() -> str:
    return os.getenv("SYSREV_API_URL", "https://sysrev.com")


@pytest.fixture(scope="module")
def project_id() -> str:
    project_id = os.getenv("SYSREV_TEST_PROJECT_ID")
    if not project_id:
        pytest.skip("SYSREV_TEST_PROJECT_ID environment variable not set")
    return project_id


@pytest.fixture(scope="module")
def authenticated_client(api_key: str, api_url: str) -> AuthenticatedClient:
    return AuthenticatedClient(base_url=api_url, token=api_key)


@pytest.fixture(scope="module")
def source_id(authenticated_client: AuthenticatedClient, project_id: str) -> str:
    source_input = CreateSourceInput(project_id=project_id)

    response = create_source.sync_detailed(
        client=authenticated_client,
        body=source_input,
    )

    assert response.status_code == 200, f"Failed to create source: {response.status_code}"
    assert response.parsed is not None, "Response parsed object is None"

    source = response.parsed
    assert hasattr(source, "id"), "Source object does not have 'id' attribute"
    assert source.id is not None, "Source ID is None"

    return source.id


@pytest.fixture
def sample_pdf_data() -> bytes:
    """
    For real tests, use an actual PDF file.
    """
    pdf_content = b"""%PDF-1.4
    1 0 obj
    <<
    /Type /Catalog
    /Pages 2 0 R
    >>
    endobj
    2 0 obj
    <<
    /Type /Pages
    /Kids [3 0 R]
    /Count 1
    >>
    endobj
    3 0 obj
    <<
    /Type /Page
    /Parent 2 0 R
    /Resources <<
    /Font <<
    /F1 <<
    /Type /Font
    /Subtype /Type1
    /BaseFont /Helvetica
    >>
    >>
    >>
    /MediaBox [0 0 612 792]
    /Contents 4 0 R
    >>
    endobj
    4 0 obj
    <<
    /Length 44
    >>
    stream
    BT
    /F1 12 Tf
    100 700 Td
    (Test PDF) Tj
    ET
    endstream
    endobj
    xref
    0 5
    0000000000 65535 f
    0000000009 00000 n
    0000000058 00000 n
    0000000115 00000 n
    0000000317 00000 n
    trailer
    <<
    /Size 5
    /Root 1 0 R
    >>
    startxref
    410
    %%EOF
    """
    return pdf_content


def test_create_source(source_id: str):
    assert source_id is not None
    assert isinstance(source_id, str)
    assert len(source_id) > 0


def test_add_article_with_json_full_text(
    authenticated_client: AuthenticatedClient,
    source_id: str,
):
    json_data = {
        "title": "Sample Article with JSON Content",
        "authors": ["John Doe", "Jane Smith"],
        "abstract": "This is a test article with JSON full text content.",
        "year": 2024,
        "sections": [
            {
                "heading": "Introduction",
                "content": "This is the introduction section.",
            },
            {
                "heading": "Methods",
                "content": "This is the methods section.",
            },
        ],
    }

    json_full_text = ArticleFullText(
        file_name="article_content.json",
        content=ArticleFullTextContentJson(json=json_data),
    )

    article_input = CreateArticleInput(
        source_id=source_id,
        citation=CreateArticleInputCitation(
            title="Sample Article with JSON Full Text",
            type_="article-journal",
        ),
        full_texts=[json_full_text],
    )

    response = create_article.sync_detailed(
        client=authenticated_client,
        body=article_input,
    )

    assert response.status_code == 200, f"Failed to create article: {response.status_code}"
    assert response.parsed is not None, "Response parsed object is None"

    article = response.parsed
    assert hasattr(article, "id"), "Article object does not have 'id' attribute"
    assert article.id is not None, "Article ID is None"
    assert hasattr(article, "title"), "Article object does not have 'title' attribute"


def test_add_article_with_pdf_full_text(
    authenticated_client: AuthenticatedClient,
    source_id: str,
    sample_pdf_data: bytes,
):
    
    pdf_base64 = base64.b64encode(sample_pdf_data).decode("utf-8")
    pdf_blob = Blob(
        mime_type="application/pdf",
        data=pdf_base64,
    )
    pdf_full_text = ArticleFullText(
        file_name="article_document.pdf",
        content=ArticleFullTextContentBlob(file_data=pdf_blob),
    )
    article_input = CreateArticleInput(
        source_id=source_id,
        citation=CreateArticleInputCitation(
            title="Sample Article with PDF Full Text",
            type_="article-journal",
        ),
        full_texts=[pdf_full_text],
    )
    response = create_article.sync_detailed(
        client=authenticated_client,
        body=article_input,
    )
    assert response.status_code == 200, f"Failed to create article: {response.status_code}"
    assert response.parsed is not None, "Response parsed object is None"

    article = response.parsed
    assert hasattr(article, "id"), "Article object does not have 'id' attribute"
    assert article.id is not None, "Article ID is None"
