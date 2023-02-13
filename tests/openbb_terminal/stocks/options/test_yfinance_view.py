# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pandas as pd
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.options import yfinance_view


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("period1", "MOCK_PERIOD_1"),
            ("period2", "MOCK_PERIOD_2"),
            ("date", "MOCK_DATE"),
        ],
    }


@pytest.mark.default_cassette("test_plot_plot")
@pytest.mark.vcr
def test_plot_plot(mocker):
    # MOCK CHARTS
    mocker.patch(
        target="openbb_terminal.stocks.options.yfinance_view.theme.visualize_output"
    )

    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.stocks.options.yfinance_view.export_data")

    yfinance_view.plot_plot(
        symbol="AAPL",
        expiry="2023-07-21",
        put=True,
        x="c",
        y="v",
        custom="smile",
        export="jpg",
    )


@pytest.mark.default_cassette("test_plot_payoff")
@pytest.mark.vcr
def test_plot_payoff(mocker):
    # MOCK CHARTS
    mocker.patch(
        target="openbb_terminal.stocks.options.yfinance_view.theme.visualize_output"
    )

    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.stocks.options.yfinance_view.export_data")

    yfinance_view.plot_payoff(
        current_price=95.0, options=[], underlying=0, symbol="AAPL", expiry="2023-07-21"
    )


@pytest.mark.default_cassette("test_show_parity")
@pytest.mark.vcr
def test_show_parity(mocker):
    # MOCK CHARTS
    mocker.patch(
        target="openbb_terminal.stocks.options.yfinance_view.theme.visualize_output"
    )

    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.stocks.options.yfinance_view.export_data")

    yfinance_view.show_parity(
        symbol="AAPL",
        expiry="2023-07-21",
        put=True,
        ask=True,
        mini=0.0,
        maxi=100.0,
        export="csv",
        sheet_name=None,
    )


@pytest.mark.default_cassette("test_risk_neutral_vals")
@pytest.mark.vcr
def test_risk_neutral_vals(mocker):
    # MOCK CHARTS
    mocker.patch(
        target="openbb_terminal.stocks.options.yfinance_view.theme.visualize_output"
    )

    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.stocks.options.yfinance_view.export_data")

    yfinance_view.risk_neutral_vals(
        symbol="AAPL",
        expiry="2023-07-21",
        put=True,
        data=pd.DataFrame(columns=["Price", "Chance"]),
        mini=None,
        maxi=None,
        risk=None,
    )


@pytest.mark.default_cassette("test_show_binom")
@pytest.mark.vcr
def test_show_binom(mocker):
    # MOCK CHARTS
    mocker.patch(
        target="openbb_terminal.stocks.options.yfinance_view.theme.visualize_output"
    )

    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.stocks.options.yfinance_view.export_data")

    # MOCK EXPORT_BINOMIAL_CALCS
    mocker.patch(target="openbb_terminal.stocks.options.yfinance_view.Workbook.save")

    yfinance_view.show_binom(
        symbol="AAPL",
        expiry="2023-07-21",
        strike=90.0,
        put=True,
        europe=False,
        export=False,
        plot=True,
        vol=None,
    )


@pytest.mark.default_cassette("test_show_greeks")
@pytest.mark.vcr
def test_show_greeks():
    yfinance_view.show_greeks(symbol="AAPL", expiry="2023-07-21", div_cont=0)
