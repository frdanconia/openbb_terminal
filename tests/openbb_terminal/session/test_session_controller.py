from unittest.mock import patch

import pytest

from openbb_terminal.session import session_controller


@pytest.mark.record_stdout
def test_display_welcome_message():
    session_controller.display_welcome_message()


@pytest.mark.record_stdout
@patch("openbb_terminal.session.session_controller.PromptSession")
def test_get_user_input(mock_prompt_session):
    mock_prompt_session().prompt.side_effect = ["test@example.com", "password", "n"]

    result = session_controller.get_user_input()

    assert result == ("test@example.com", "password", False)


@pytest.mark.record_stdout
@patch("openbb_terminal.session.session_controller.PromptSession")
def test_get_user_input_with_save(mock_prompt_session):
    mock_prompt_session().prompt.side_effect = ["test@example.com", "password", "y"]

    result = session_controller.get_user_input()

    assert result == ("test@example.com", "password", True)


def test_prompt():
    with patch(
        "openbb_terminal.session.session_controller.get_user_input",
        return_value=("email", "password", False),
    ) as get_user_input_mock, patch(
        "openbb_terminal.session.session_controller.create_session",
        return_value={"session": "session"},
    ) as create_session_mock, patch(
        "openbb_terminal.session.session_controller.login_and_launch",
        return_value=True,
    ):
        session_controller.prompt()
        assert get_user_input_mock.call_count == 1
        create_session_mock.assert_called_once_with("email", "password", False)
        assert create_session_mock.call_count == 1


def test_prompt_guest_allowed():
    with patch(
        "openbb_terminal.session.session_controller.get_user_input",
        return_value=(None, None, False),
    ) as get_user_input_mock, patch(
        "openbb_terminal.session.session_controller.launch_terminal", return_value=True
    ) as launch_terminal_mock:
        session_controller.prompt(guest_allowed=True)
        assert get_user_input_mock.call_count == 1
        assert launch_terminal_mock.call_count == 1


def test_launch_terminal():
    with patch(
        "openbb_terminal.session.session_controller.terminal_controller.parse_args_and_run",
        return_value=True,
    ) as parse_args_mock:
        session_controller.launch_terminal()
        assert parse_args_mock.call_count == 1


def test_login_and_launch():
    with patch(
        "openbb_terminal.session.session_controller.login",
        return_value=session_controller.LoginStatus.SUCCESS,
    ) as login_mock, patch(
        "openbb_terminal.session.session_controller.launch_terminal", return_value=True
    ) as launch_terminal_mock:
        session_controller.login_and_launch(session={})
        assert login_mock.call_count == 1
        assert launch_terminal_mock.call_count == 1


def test_login_and_launch_failed():
    with patch(
        "openbb_terminal.session.session_controller.login",
        return_value=session_controller.LoginStatus.FAILED,
    ) as login_mock, patch(
        "openbb_terminal.session.session_controller.prompt", return_value=True
    ) as prompt_mock:
        session_controller.login_and_launch(session={})
        assert login_mock.call_count == 1
        assert prompt_mock.call_count == 1


def test_login_and_launch_no_response():
    with patch(
        "openbb_terminal.session.session_controller.login",
        return_value=session_controller.LoginStatus.NO_RESPONSE,
    ) as login_mock, patch(
        "openbb_terminal.session.session_controller.prompt", return_value=True
    ) as prompt_mock:
        session_controller.login_and_launch(session={})
        assert login_mock.call_count == 1
        assert prompt_mock.call_count == 1


def test_main_local_session():
    with patch(
        "openbb_terminal.session.session_controller.prompt", return_value=True
    ) as prompt_mock, patch(
        "openbb_terminal.session.session_controller.Local.get_session",
        return_value=False,
    ) as get_session_mock:
        session_controller.main()
        assert prompt_mock.call_count == 1
        assert get_session_mock.call_count == 1


def test_main_no_local_session():
    with patch(
        "openbb_terminal.session.session_controller.login_and_launch", return_value=True
    ) as login_and_launch_mock, patch(
        "openbb_terminal.session.session_controller.Local.get_session",
        return_value=True,
    ) as get_session_mock:
        session_controller.main()
        assert login_and_launch_mock.call_count == 1
        assert get_session_mock.call_count == 1
