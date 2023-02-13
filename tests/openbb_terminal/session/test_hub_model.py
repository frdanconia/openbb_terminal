from unittest.mock import MagicMock, patch

import pytest
import requests

from openbb_terminal.session import hub_model

TEST_RESPONSE = {
    "access_token": "test_token",
    "token_type": "bearer",
    "uuid": "test_uuid",
}

TEST_EMAIL_PASSWORD = [
    (
        "test_email",
        "test_pass",
    ),
]

TEST_HEADER_TOKEN = [
    ("Bearer test_token", "test_token"),
]


@pytest.mark.parametrize("email, password", TEST_EMAIL_PASSWORD)
def test_create_session_success(email, password):
    with patch("requests.post") as mock_post:
        mock_post.return_value.json.return_value = TEST_RESPONSE
        response = hub_model.create_session(email, password)
        assert response.json() == TEST_RESPONSE

        mock_post.assert_called_once_with(
            url=hub_model.BASE_URL + "login",
            json={"email": email, "password": password, "remember": True},
            timeout=hub_model.TIMEOUT,
        )


@pytest.mark.parametrize("email, password", TEST_EMAIL_PASSWORD)
def test_create_session_connection_error(email, password):
    with patch("requests.post") as mock_post:
        mock_post.side_effect = requests.exceptions.ConnectionError
        response = hub_model.create_session(email, password)
        assert response is None


@pytest.mark.parametrize("email, password", TEST_EMAIL_PASSWORD)
def test_create_session_timeout(email, password):
    with patch("requests.post") as mock_post:
        mock_post.side_effect = requests.exceptions.Timeout
        response = hub_model.create_session(email, password)
        assert response is None


@pytest.mark.parametrize("email, password", TEST_EMAIL_PASSWORD)
def test_create_session_exception(email, password):
    with patch("requests.post") as mock_post:
        mock_post.side_effect = Exception
        response = hub_model.create_session(email, password)
        assert response is None


@pytest.mark.parametrize("auth_header, token", TEST_HEADER_TOKEN)
def test_delete_session_success(auth_header, token):
    with patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        response = hub_model.delete_session(auth_header, token)
        assert response.status_code == 200

        mock_post.assert_called_once_with(
            url=hub_model.BASE_URL + "logout",
            headers={"Authorization": "Bearer test_token"},
            json={"token": "test_token"},
            timeout=hub_model.TIMEOUT,
        )


@pytest.mark.parametrize("auth_header, token", TEST_HEADER_TOKEN)
def test_delete_session_connection_error(auth_header, token):
    with patch("requests.post") as mock_post:
        mock_post.side_effect = requests.exceptions.ConnectionError
        response = hub_model.delete_session(auth_header, token)
        assert response is None


@pytest.mark.parametrize("auth_header, token", TEST_HEADER_TOKEN)
def test_delete_session_timeout(auth_header, token):
    with patch("requests.post") as mock_post:
        mock_post.side_effect = requests.exceptions.Timeout
        response = hub_model.delete_session(auth_header, token)
        assert response is None


@pytest.mark.parametrize("auth_header, token", TEST_HEADER_TOKEN)
def test_delete_session_exception(auth_header, token):
    with patch("requests.post") as mock_post:
        mock_post.side_effect = Exception
        response = hub_model.delete_session(auth_header, token)
        assert response is None


def test_process_session_response_success():
    response = requests.Response()
    response.status_code = 200
    response.json = lambda: {
        "access_token": "test_token",
        "token_type": "bearer",
        "uuid": "test_uuid",
    }
    login = hub_model.process_session_response(response)
    assert login == {
        "access_token": "test_token",
        "token_type": "bearer",
        "uuid": "test_uuid",
    }


def test_process_session_response_401():
    response = requests.Response()
    response.status_code = 401
    login = hub_model.process_session_response(response)
    assert not login
    assert isinstance(login, dict)


def test_process_session_response_403():
    response = requests.Response()
    response.status_code = 403
    login = hub_model.process_session_response(response)
    assert not login
    assert isinstance(login, dict)


def test_process_session_response_fail():
    response = requests.Response()
    response.status_code = 400
    login = hub_model.process_session_response(response)
    assert not login
    assert isinstance(login, dict)


def test_get_session_success():
    mock_response = MagicMock(spec=requests.Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {"session": "info"}

    with patch(
        "openbb_terminal.session.hub_model.create_session", return_value=mock_response
    ) as create_session_mock:
        result = hub_model.get_session("email", "password")
        assert result == {"session": "info"}
        create_session_mock.assert_called_once_with("email", "password")


def test_get_session_401():
    mock_response = MagicMock(spec=requests.Response)
    mock_response.status_code = 401

    with patch(
        "openbb_terminal.session.hub_model.create_session", return_value=mock_response
    ) as create_session_mock:
        result = hub_model.get_session("email", "password")
        assert result == {}
        create_session_mock.assert_called_once_with("email", "password")


def test_get_session_403():
    mock_response = MagicMock(spec=requests.Response)
    mock_response.status_code = 403

    with patch(
        "openbb_terminal.session.hub_model.create_session", return_value=mock_response
    ) as create_session_mock:
        result = hub_model.get_session("email", "password")
        assert result == {}
        create_session_mock.assert_called_once_with("email", "password")


def test_get_session_failed_to_request():
    with patch(
        "openbb_terminal.session.hub_model.create_session", return_value=None
    ) as create_session_mock:
        result = hub_model.get_session("email", "password")
        assert result == {}
        create_session_mock.assert_called_once_with("email", "password")


@pytest.mark.parametrize("token_type, access_token", [("TokenType", "AccessToken")])
def test_fetch_user_configs_success(token_type, access_token):
    mock_response = MagicMock(spec=requests.Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {"configs": "info"}

    with patch(
        "openbb_terminal.session.hub_model.requests.get", return_value=mock_response
    ) as requests_get_mock:
        session = {"token_type": token_type, "access_token": access_token}
        result = hub_model.fetch_user_configs(session)
        assert result == mock_response
        requests_get_mock.assert_called_once()
        _, kwargs = requests_get_mock.call_args
        assert kwargs["url"] == hub_model.BASE_URL + "terminal/user"
        assert kwargs["headers"] == {
            "Authorization": f"{token_type.title()} {access_token}"
        }
        assert kwargs["timeout"] == hub_model.TIMEOUT


def test_fetch_user_configs_failure():
    mock_response = MagicMock(spec=requests.Response)
    mock_response.status_code = 404

    with patch("requests.get", return_value=mock_response) as get_mock:
        session = {"token_type": "Bearer", "access_token": "abc123"}
        result = hub_model.fetch_user_configs(session)
        assert isinstance(result, requests.Response)
        get_mock.assert_called_once_with(
            url=hub_model.BASE_URL + "terminal/user",
            headers={"Authorization": "Bearer abc123"},
            timeout=hub_model.TIMEOUT,
        )


def test_fetch_user_configs_connection_error():
    with patch(
        "requests.get", side_effect=requests.exceptions.ConnectionError
    ) as get_mock:
        session = {"token_type": "Bearer", "access_token": "abc123"}
        result = hub_model.fetch_user_configs(session)
        assert result is None
        get_mock.assert_called_once_with(
            url=hub_model.BASE_URL + "terminal/user",
            headers={"Authorization": "Bearer abc123"},
            timeout=hub_model.TIMEOUT,
        )


def test_fetch_user_configs_timeout():
    with patch("requests.get", side_effect=requests.exceptions.Timeout) as get_mock:
        session = {"token_type": "Bearer", "access_token": "abc123"}
        result = hub_model.fetch_user_configs(session)
        assert result is None
        get_mock.assert_called_once_with(
            url=hub_model.BASE_URL + "terminal/user",
            headers={"Authorization": "Bearer abc123"},
            timeout=hub_model.TIMEOUT,
        )


def test_fetch_user_configs_exception():
    with patch("requests.get", side_effect=Exception) as get_mock:
        session = {"token_type": "Bearer", "access_token": "abc123"}
        result = hub_model.fetch_user_configs(session)
        assert result is None
        get_mock.assert_called_once_with(
            url=hub_model.BASE_URL + "terminal/user",
            headers={"Authorization": "Bearer abc123"},
            timeout=hub_model.TIMEOUT,
        )


@pytest.mark.parametrize(
    "key, value, type_, auth_header",
    [
        ("key", "value", "keys", "auth_header"),
        ("key", "value", "settings", "auth_header"),
    ],
)
def test_patch_user_configs_success(key, value, type_, auth_header):
    mock_response = MagicMock(spec=requests.Response)
    mock_response.status_code = 200

    with patch(
        "openbb_terminal.session.hub_model.requests.patch", return_value=mock_response
    ) as requests_patch_mock:
        result = hub_model.patch_user_configs(key, value, type_, auth_header)

        assert result.status_code == mock_response.status_code
        requests_patch_mock.assert_called_once()
        _, kwargs = requests_patch_mock.call_args
        assert kwargs["url"] == hub_model.BASE_URL + "terminal/user"
        assert kwargs["headers"] == {"Authorization": f"{auth_header}"}
        assert kwargs["json"] == {"key": f"features_{type_}.{key}", "value": value}
        assert kwargs["timeout"] == hub_model.TIMEOUT


def test_patch_user_configs_failure():
    mock_response = MagicMock(spec=requests.Response)
    mock_response.status_code = 400

    with patch(
        "openbb_terminal.session.hub_model.requests.patch", return_value=mock_response
    ) as requests_patch_mock:
        result = hub_model.patch_user_configs("key", "value", "keys", "auth_header")

        assert result.status_code == mock_response.status_code
        requests_patch_mock.assert_called_once()
        _, kwargs = requests_patch_mock.call_args
        assert kwargs["url"] == hub_model.BASE_URL + "terminal/user"
        assert kwargs["headers"] == {"Authorization": "auth_header"}
        assert kwargs["json"] == {"key": "features_keys.key", "value": "value"}
        assert kwargs["timeout"] == hub_model.TIMEOUT


def test_patch_user_configs_connection_error():
    with patch(
        "openbb_terminal.session.hub_model.requests.patch"
    ) as requests_patch_mock:
        requests_patch_mock.side_effect = requests.exceptions.ConnectionError()

        result = hub_model.patch_user_configs("key", "value", "keys", "auth_header")

        assert result is None
        requests_patch_mock.assert_called_once()
        _, kwargs = requests_patch_mock.call_args
        assert kwargs["url"] == hub_model.BASE_URL + "terminal/user"
        assert kwargs["headers"] == {"Authorization": "auth_header"}
        assert kwargs["json"] == {"key": "features_keys.key", "value": "value"}
        assert kwargs["timeout"] == hub_model.TIMEOUT


def test_patch_user_configs_timeout():
    with patch(
        "openbb_terminal.session.hub_model.requests.patch"
    ) as requests_patch_mock:
        requests_patch_mock.side_effect = requests.exceptions.Timeout()

        result = hub_model.patch_user_configs("key", "value", "keys", "auth_header")

        assert result is None
        requests_patch_mock.assert_called_once()
        _, kwargs = requests_patch_mock.call_args
        assert kwargs["url"] == hub_model.BASE_URL + "terminal/user"
        assert kwargs["headers"] == {"Authorization": "auth_header"}
        assert kwargs["json"] == {"key": "features_keys.key", "value": "value"}
        assert kwargs["timeout"] == hub_model.TIMEOUT


def test_patch_user_configs_exception():
    with patch(
        "openbb_terminal.session.hub_model.requests.patch"
    ) as requests_patch_mock:
        requests_patch_mock.side_effect = Exception()

        result = hub_model.patch_user_configs("key", "value", "keys", "auth_header")

        assert result is None
        requests_patch_mock.assert_called_once()
        _, kwargs = requests_patch_mock.call_args
        assert kwargs["url"] == hub_model.BASE_URL + "terminal/user"
        assert kwargs["headers"] == {"Authorization": "auth_header"}
        assert kwargs["json"] == {"key": "features_keys.key", "value": "value"}
        assert kwargs["timeout"] == hub_model.TIMEOUT


def test_clear_user_configs_success():
    mock_response = MagicMock(spec=requests.Response)
    mock_response.status_code = 200

    with patch(
        "openbb_terminal.session.hub_model.requests.put", return_value=mock_response
    ) as requests_put_mock:
        result = hub_model.clear_user_configs("auth_header")

        assert result.status_code == mock_response.status_code
        requests_put_mock.assert_called_once()
        _, kwargs = requests_put_mock.call_args
        assert kwargs["url"] == hub_model.BASE_URL + "terminal/user"
        assert kwargs["headers"] == {"Authorization": "auth_header"}
        assert kwargs["json"] == {"features_keys": {}, "features_settings": {}}
        assert kwargs["timeout"] == hub_model.TIMEOUT


def test_clear_user_configs_failure():
    mock_response = MagicMock(spec=requests.Response)
    mock_response.status_code = 400

    with patch(
        "openbb_terminal.session.hub_model.requests.put", return_value=mock_response
    ) as requests_put_mock:
        result = hub_model.clear_user_configs("auth_header")

        assert result.status_code == mock_response.status_code
        requests_put_mock.assert_called_once()
        _, kwargs = requests_put_mock.call_args
        assert kwargs["url"] == hub_model.BASE_URL + "terminal/user"
        assert kwargs["headers"] == {"Authorization": "auth_header"}
        assert kwargs["json"] == {"features_keys": {}, "features_settings": {}}
        assert kwargs["timeout"] == hub_model.TIMEOUT


def test_clear_user_configs_timeout():
    with patch(
        "openbb_terminal.session.hub_model.requests.put",
        side_effect=requests.exceptions.Timeout,
    ) as requests_put_mock:
        result = hub_model.clear_user_configs("auth_header")

        assert result is None
        requests_put_mock.assert_called_once()
        _, kwargs = requests_put_mock.call_args
        assert kwargs["url"] == hub_model.BASE_URL + "terminal/user"
        assert kwargs["headers"] == {"Authorization": "auth_header"}
        assert kwargs["json"] == {"features_keys": {}, "features_settings": {}}
        assert kwargs["timeout"] == hub_model.TIMEOUT


def test_clear_user_configs_connection_error():
    with patch("openbb_terminal.session.hub_model.requests.put") as requests_put_mock:
        requests_put_mock.side_effect = requests.exceptions.ConnectionError()
        result = hub_model.clear_user_configs("auth_header")

        assert result is None
        requests_put_mock.assert_called_once()
        _, kwargs = requests_put_mock.call_args
        assert kwargs["url"] == hub_model.BASE_URL + "terminal/user"
        assert kwargs["headers"] == {"Authorization": "auth_header"}
        assert kwargs["json"] == {"features_keys": {}, "features_settings": {}}
        assert kwargs["timeout"] == hub_model.TIMEOUT


def test_clear_user_configs_exception():
    with patch(
        "openbb_terminal.session.hub_model.requests.put", side_effect=Exception
    ) as requests_put_mock:
        result = hub_model.clear_user_configs("auth_header")

        assert result is None
        requests_put_mock.assert_called_once()
        _, kwargs = requests_put_mock.call_args
        assert kwargs["url"] == hub_model.BASE_URL + "terminal/user"
        assert kwargs["headers"] == {"Authorization": "auth_header"}
        assert kwargs["json"] == {"features_keys": {}, "features_settings": {}}
        assert kwargs["timeout"] == hub_model.TIMEOUT


@pytest.mark.parametrize(
    "auth_header, name, description, routine, override, base_url, timeout, status_code",
    [
        ("auth_header", "name", "description", "routine", True, "base_url", 10, 200),
        ("auth_header", "name", "description", "routine", False, "base_url", 10, 400),
    ],
)
def test_upload_routine(
    auth_header, name, description, routine, override, base_url, timeout, status_code
):
    mock_response = MagicMock(spec=requests.Response)
    mock_response.status_code = status_code

    with patch(
        "openbb_terminal.session.hub_model.requests.post", return_value=mock_response
    ) as requests_get_mock:
        result = hub_model.upload_routine(
            auth_header=auth_header,
            name=name,
            description=description,
            routine=routine,
            override=override,
            base_url=base_url,
            timeout=timeout,
        )

        assert result.status_code == mock_response.status_code
        requests_get_mock.assert_called_once()
        _, kwargs = requests_get_mock.call_args
        assert kwargs["url"] == base_url + "terminal/script"
        assert kwargs["headers"] == {"Authorization": auth_header}
        assert kwargs["timeout"] == timeout


@pytest.mark.parametrize(
    "side_effect",
    [
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
        Exception,
    ],
)
def test_upload_routine_error(side_effect):
    with patch(
        "openbb_terminal.session.hub_model.requests.post",
        side_effect=side_effect,
    ):
        result = hub_model.upload_routine("auth_header", "name", "routine")
        assert result is None


@pytest.mark.parametrize(
    "auth_header, name, base_url, timeout, status_code",
    [
        ("auth_header", "name", "base_url", 10, 200),
        ("other_header", "other name", "other_url", 10, 400),
    ],
)
def test_download_routine(auth_header, name, base_url, timeout, status_code):
    mock_response = MagicMock(spec=requests.Response)
    mock_response.status_code = status_code

    with patch(
        "openbb_terminal.session.hub_model.requests.get", return_value=mock_response
    ) as requests_get_mock:
        result = hub_model.download_routine(
            auth_header=auth_header, name=name, base_url=base_url, timeout=timeout
        )

        assert result.status_code == mock_response.status_code
        requests_get_mock.assert_called_once()
        _, kwargs = requests_get_mock.call_args
        assert kwargs["url"] == base_url + f"terminal/script/{name}"
        assert kwargs["headers"] == {"Authorization": auth_header}
        assert kwargs["timeout"] == timeout


@pytest.mark.parametrize(
    "side_effect",
    [
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
        Exception,
    ],
)
def test_download_routine_error(side_effect):
    with patch(
        "openbb_terminal.session.hub_model.requests.get",
        side_effect=side_effect,
    ):
        result = hub_model.download_routine("auth_header", "name", "routine")
        assert result is None


@pytest.mark.parametrize(
    "auth_header, name, base_url, timeout, status_code",
    [
        ("auth_header", "name", "base_url", 10, 200),
        ("other_header", "other name", "other_url", 10, 400),
    ],
)
def test_delete_routine(auth_header, name, base_url, timeout, status_code):
    mock_response = MagicMock(spec=requests.Response)
    mock_response.status_code = status_code

    with patch(
        "openbb_terminal.session.hub_model.requests.delete", return_value=mock_response
    ) as requests_get_mock:
        result = hub_model.delete_routine(
            auth_header=auth_header, name=name, base_url=base_url, timeout=timeout
        )

        assert result.status_code == mock_response.status_code
        requests_get_mock.assert_called_once()
        _, kwargs = requests_get_mock.call_args
        assert kwargs["url"] == base_url + f"terminal/script/{name}"
        assert kwargs["headers"] == {"Authorization": auth_header}
        assert kwargs["timeout"] == timeout


@pytest.mark.parametrize(
    "side_effect",
    [
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
        Exception,
    ],
)
def test_delete_routine_error(side_effect):
    with patch(
        "openbb_terminal.session.hub_model.requests.delete",
        side_effect=side_effect,
    ):
        result = hub_model.delete_routine("auth_header", "name")
        assert result is None


@pytest.mark.parametrize(
    "auth_header, page, size, base_url, timeout, status_code",
    [
        ("auth_header", 1, 10, "base_url", 10, 200),
        ("other_header", 2, 20, "other_url", 10, 400),
    ],
)
def test_list_routines(auth_header, page, size, base_url, timeout, status_code):
    mock_response = MagicMock(spec=requests.Response)
    mock_response.status_code = status_code

    with patch(
        "openbb_terminal.session.hub_model.requests.get", return_value=mock_response
    ) as requests_get_mock:
        result = hub_model.list_routines(
            auth_header=auth_header,
            page=page,
            size=size,
            base_url=base_url,
            timeout=timeout,
        )

        assert result.status_code == mock_response.status_code
        requests_get_mock.assert_called_once()
        _, kwargs = requests_get_mock.call_args
        assert (
            kwargs["url"]
            == base_url
            + f"terminal/script?fields=name%2Cdescription&page={page}&size={size}"
        )
        assert kwargs["headers"] == {"Authorization": auth_header}
        assert kwargs["timeout"] == timeout


@pytest.mark.parametrize(
    "side_effect",
    [
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
        Exception,
    ],
)
def test_list_routines_error(side_effect):
    with patch(
        "openbb_terminal.session.hub_model.requests.get",
        side_effect=side_effect,
    ):
        result = hub_model.list_routines(auth_header="Bearer 123", page=1, size=10)
        assert result is None
