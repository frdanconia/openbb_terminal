import pandas as pd
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.options import intrinio_model


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_query_parameters": [
            ("api_key", "MOCK_API_KEY"),
            ("before", "MOCK_BEFORE"),
            ("after", "MOCK_AFTER"),
        ]
    }


@pytest.mark.vcr
def test_get_option_chain(recorder):
    df = intrinio_model.get_option_chain("AAPL", "2025-01-17")
    recorder.capture(df)


@pytest.mark.vcr
def test_get_full_option_chain(recorder):
    df = intrinio_model.get_full_option_chain("AAPL")
    recorder.capture(df)


@pytest.mark.vcr
def test_get_expirations(recorder):
    exps = intrinio_model.get_expiration_dates(
        "AAPL", start="2023-01-01", end="2025-01-01"
    )
    recorder.capture(exps)


@pytest.mark.vcr
def test_get_eod_chain(recorder):
    df = intrinio_model.get_eod_chain_at_expiry_given_date(
        "AAPL", "2025-01-17", date="2022-12-27"
    )
    recorder.capture(df)


@pytest.mark.vcr
def test_get_full_chain_eod(recorder):
    df = intrinio_model.get_full_chain_eod("AAPL", "2022-12-27")
    recorder.capture(df)


@pytest.mark.vcr
def test_get_close_at_date(recorder):
    close = intrinio_model.get_close_at_date("AAPL", "2022-12-27")
    recorder.capture(close)


def test_calculate_dte():
    sample_df = pd.DataFrame(
        {
            "expiration": ["2027-12-12", "2023-01-02", "2024-12-12", "2023-01-02"],
            "date": ["2024-12-12", "2023-01-02", "2024-12-11", "2022-11-02"],
        }
    )
    new_df = intrinio_model.calculate_dte(sample_df)
    assert "dte" in new_df.columns
    assert new_df["dte"].tolist() == [1095 / 365, 0, 1 / 365, 61 / 365]
    pd.testing.assert_frame_equal(new_df[sample_df.columns], new_df)


@pytest.mark.vcr
def test_option_chain_bad_symbol(recorder):
    df = intrinio_model.get_option_chain("BAD_SYMBOL", "2025-01-17")
    recorder.capture(df)
    assert df.empty
    df2 = intrinio_model.get_eod_chain_at_expiry_given_date(
        "BAD_SYMBOL", "2025-01-17", "2022-12-27"
    )
    recorder.capture(df2)
    assert df2.empty
