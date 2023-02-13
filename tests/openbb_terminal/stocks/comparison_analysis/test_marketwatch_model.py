# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.comparison_analysis import marketwatch_model


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
    }


@pytest.mark.vcr
@pytest.mark.parametrize(
    "timeframe, quarter",
    [
        ("31-Dec-2021", True),
        ("2020", False),
    ],
)
def test_get_financial_comparisons(quarter, timeframe, recorder):
    result_df = marketwatch_model.get_financial_comparisons(
        symbols=["TSLA", "GM"],
        data="income",
        timeframe=timeframe,
        quarter=quarter,
    )

    recorder.capture(result_df)
