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


def test_can_import_api_endpoints():
    from sysrev_client.lib import api

    assert hasattr(api, "article")
    assert hasattr(api, "project")
    assert hasattr(api, "user")
    assert hasattr(api, "label")
