# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.screener import yahoofinance_model, yahoofinance_view


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("period1", "1598220000"),
            ("period2", "1635980400"),
        ],
    }


@pytest.mark.vcr
@pytest.mark.record_stdout
def test_historical(mocker):
    # FORCE SINGLE THREADING
    yf_download = yahoofinance_model.yf.download

    def mock_yf_download(*args, **kwargs):
        kwargs["threads"] = False
        return yf_download(*args, **kwargs)

    mocker.patch(
        "openbb_terminal.stocks.screener.yahoofinance_model.yf.download",
        side_effect=mock_yf_download,
    )

    # MOCK VISUALIZE_OUTPUT
    mocker.patch(target="openbb_terminal.helper_classes.TerminalStyle.visualize_output")

    # MOCK EXPORT_DATA
    mocker.patch(
        target="openbb_terminal.stocks.screener.finviz_view.export_data",
    )

    # MOCK PROGRESS_BAR
    mocker.patch(
        target="finvizfinance.screener.overview.progress_bar",
    )

    # MOCK EXPORT_DATA
    mocker.patch(
        target="random.shuffle",
    )

    yahoofinance_view.historical(
        preset_loaded="top_gainers",
        limit=2,
        start_date="2022-01-03",
        type_candle="a",
        normalize=True,
        export="",
    )


@pytest.mark.vcr
@pytest.mark.record_stdout
def test_historical_no_d_signals(mocker):
    # FORCE SINGLE THREADING
    yf_download = yahoofinance_model.yf.download

    def mock_yf_download(*args, **kwargs):
        kwargs["threads"] = False
        return yf_download(*args, **kwargs)

    mocker.patch(
        "openbb_terminal.stocks.screener.yahoofinance_model.yf.download",
        side_effect=mock_yf_download,
    )

    # MOCK VISUALIZE_OUTPUT
    mocker.patch(target="openbb_terminal.helper_classes.TerminalStyle.visualize_output")

    # MOCK EXPORT_DATA
    mocker.patch(
        target="openbb_terminal.stocks.screener.finviz_view.export_data",
    )

    # MOCK PROGRESS_BAR
    mocker.patch(
        target="finvizfinance.screener.overview.progress_bar",
    )

    # MOCK EXPORT_DATA
    mocker.patch(
        target="random.shuffle",
    )

    # MOCK D_SIGNALS
    mocker.patch.object(
        target=yahoofinance_model.finviz_model,
        attribute="d_signals",
        new=[],
    )

    yahoofinance_view.historical(
        preset_loaded="oversold.ini",
        limit=2,
        start_date="2022-01-03",
        type_candle="a",
        normalize=True,
        export="",
    )
