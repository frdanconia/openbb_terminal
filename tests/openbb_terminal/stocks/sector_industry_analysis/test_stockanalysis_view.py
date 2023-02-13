# pylint: disable=too-many-arguments

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.sector_industry_analysis import stockanalysis_view


@pytest.mark.skip
@pytest.mark.vcr
@pytest.mark.parametrize(
    "finance_key, country, sector, industry, period, period_length, marketcap, statement",
    [
        (
            "re",
            "United States",
            None,
            "Credit Services",
            "annual",
            12,
            "Large",
            "IS",
        ),
        (
            "rec",
            "Germany",
            "Technology",
            None,
            "trailing",
            13,
            "Large",
            "BS",
        ),
        (
            "ncf",
            "Netherlands",
            "Technology",
            None,
            "annual",
            3,
            "Large",
            "CF",
        ),
    ],
)
def test_display_plots_financials(
    recorder,
    mocker,
    finance_key,
    country,
    sector,
    industry,
    period,
    period_length,
    marketcap,
    statement,
):
    mocker.patch(
        target="openbb_terminal.stocks.sector_industry_analysis.stockanalysis_view.plt.show"
    )
    mocker.patch(
        target="openbb_terminal.stocks.sector_industry_analysis.stockanalysis_view.export_data"
    )
    stocks_data, company_tickers = stockanalysis_view.display_plots_financials(
        finance_key=finance_key,
        country=country,
        sector=sector,
        industry=industry,
        period=period,
        period_length=period_length,
        marketcap=marketcap,
    )

    recorder.capture(company_tickers)
    recorder.capture_list(stocks_data[statement].values())
