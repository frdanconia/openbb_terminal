# IMPORTATION STANDARD
from datetime import datetime

# IMPORTATION THIRDPARTY
import pandas as pd
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks import stocks_helper
from openbb_terminal.stocks.dark_pool_shorts import sec_view

df_fails_to_deliver = pd.DataFrame(
    data={
        "SETTLEMENT DATE": [
            pd.Timestamp("2021-11-26 00:00:00"),
            pd.Timestamp("2021-11-30 00:00:00"),
        ],
        "QUANTITY (FAILS)": [27, 2440],
    }
)


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
@pytest.mark.parametrize(
    "raw",
    [True, False],
)
def test_fails_to_deliver(mocker, raw):
    # MOCK VISUALIZE_OUTPUT
    mocker.patch(target="openbb_terminal.helper_classes.TerminalStyle.visualize_output")

    mocker.patch(
        target="openbb_terminal.stocks.dark_pool_shorts.sec_model.get_fails_to_deliver",
        new=mocker.Mock(return_value=df_fails_to_deliver.copy()),
    )
    stock = stocks_helper.load(
        symbol="TSLA",
        start_date=datetime.strptime("2021-12-18", "%Y-%m-%d"),
    )

    sec_view.fails_to_deliver(
        symbol="PM",
        data=stock,
        start_date=datetime.strptime("2021-12-18", "%Y-%m-%d"),
        end_date=datetime.strptime("2021-12-19", "%Y-%m-%d"),
        limit=2,
        raw=raw,
        export="",
        sheet_name=None,
    )
