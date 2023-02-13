import pytest

from openbb_terminal.cryptocurrency.overview import pycoingecko_view

# pylint: disable=unused-import


# pylint: disable=R0904
@pytest.mark.skip
@pytest.mark.record_stdout
@pytest.mark.vcr()
def test_coin_holdings_overview():
    pycoingecko_view.display_holdings_overview(
        symbol="bitcoin", show_bar=False, export="", limit=20
    )


@pytest.mark.record_stdout
@pytest.mark.vcr()
def test_coin_categories():
    pycoingecko_view.display_categories(
        limit=15, export="", pie=False, sortby="market_cap"
    )


@pytest.mark.record_stdout
@pytest.mark.vcr()
def test_coin_stablecoins():
    pycoingecko_view.display_stablecoins(
        limit=15, export="", sortby="Market_Cap_[$]", pie=False, ascend=False
    )


@pytest.mark.record_stdout
@pytest.mark.vcr()
def test_coin_exchanges():
    pycoingecko_view.display_exchanges(
        limit=15, sortby="Rank", ascend=True, links=False, export=""
    )


@pytest.mark.record_stdout
@pytest.mark.vcr()
def test_coin_indexes():
    pycoingecko_view.display_indexes(limit=15, ascend=True, export="")


@pytest.mark.record_stdout
@pytest.mark.vcr()
def test_coin_derivatives():
    pycoingecko_view.display_derivatives(
        limit=15, sortby="Rank", ascend=True, export=""
    )


@pytest.mark.record_stdout
@pytest.mark.vcr()
def test_coin_exchange_rates():
    pycoingecko_view.display_exchange_rates(
        limit=15, sortby="Index", ascend=True, export=""
    )


@pytest.mark.record_stdout
@pytest.mark.vcr()
def test_coin_global_market_info():
    pycoingecko_view.display_global_market_info(export="", pie=False)


@pytest.mark.record_stdout
@pytest.mark.vcr()
def test_coin_global_defi_info():
    pycoingecko_view.display_global_defi_info(export="")
