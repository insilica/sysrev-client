def test_can_import_client_classes():
    from sysrev_client.lib import AuthenticatedClient, Client

    assert AuthenticatedClient is not None
    assert Client is not None


def test_can_import_models():
    from sysrev_client.lib import Article, Project, User

    assert Article is not None
    assert Project is not None
    assert User is not None


def test_can_import_errors():
    from sysrev_client.lib import UnexpectedStatus

    assert UnexpectedStatus is not None


def test_can_import_types():
    from sysrev_client.lib import File, Response, UNSET

    assert File is not None
    assert Response is not None
    assert UNSET is not None


def test_can_import_api_endpoint_modules():
    from sysrev_client.lib import (
        create_article,
        get_article,
        create_project,
        get_project,
        get_user,
        get_label,
    )

    assert create_article is not None
    assert get_article is not None
    assert create_project is not None
    assert get_project is not None
    assert get_user is not None
    assert get_label is not None


def test_endpoint_modules_have_expected_functions():
    from sysrev_client.lib import create_article, get_article

    assert hasattr(create_article, "sync")
    assert hasattr(create_article, "sync_detailed")
    assert hasattr(create_article, "asyncio")
    assert hasattr(create_article, "asyncio_detailed")

    assert hasattr(get_article, "sync")
    assert hasattr(get_article, "sync_detailed")
    assert hasattr(get_article, "asyncio")
    assert hasattr(get_article, "asyncio_detailed")
