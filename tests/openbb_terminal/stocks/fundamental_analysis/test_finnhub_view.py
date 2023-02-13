# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.fundamental_analysis import finnhub_view


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_query_parameters": [
            ("token", "MOCK_TOKEN"),
        ]
    }


@pytest.mark.default_cassette("test_rating_over_time_TSLA")
@pytest.mark.vcr
@pytest.mark.record_stdout
def test_rating_over_time(mocker):
    # MOCK VISUALIZE_OUTPUT
    mocker.patch(target="openbb_terminal.helper_classes.TerminalStyle.visualize_output")
    finnhub_view.rating_over_time(
        symbol="TSLA",
        limit=10,
        raw=True,
        export=None,
    )


@pytest.mark.default_cassette("test_rating_over_time_TSLA")
@pytest.mark.vcr(mode="none")
def test_rating_over_time_plt(capsys, mocker):
    # MOCK VISUALIZE_OUTPUT
    mocker.patch(target="openbb_terminal.helper_classes.TerminalStyle.visualize_output")

    finnhub_view.rating_over_time(
        symbol="TSLA",
        limit=10,
        raw=False,
        export=None,
    )

    capsys.readouterr()


@pytest.mark.vcr
@pytest.mark.record_stdout
def test_rating_over_time_invalid_ticker(mocker):
    # MOCK VISUALIZE_OUTPUT
    mocker.patch(target="openbb_terminal.helper_classes.TerminalStyle.visualize_output")

    finnhub_view.rating_over_time(
        symbol="INVALID_TICKER",
        limit=10,
        raw=False,
        export=None,
    )


@pytest.mark.vcr
@pytest.mark.record_stdout
def test_rating_over_time_invalid_token(mocker):
    # MOCK VISUALIZE_OUTPUT
    mocker.patch(target="openbb_terminal.helper_classes.TerminalStyle.visualize_output")
    finnhub_view.rating_over_time(
        symbol="TSLA",
        limit=10,
        raw=False,
        export=None,
    )
