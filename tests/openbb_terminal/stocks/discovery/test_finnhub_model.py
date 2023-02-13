# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.discovery import finnhub_model


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_query_parameters": [
            ("from", "MOCK_FROM"),
            ("to", "MOCK_TO"),
            ("token", "MOCK_TOKEN"),
        ]
    }


@pytest.mark.vcr
def test_get_ipo_calendar(recorder):
    ipo_df = finnhub_model.get_ipo_calendar(
        start_date="2021-12-01",
        end_date="2021-12-02",
    )
    recorder.capture(ipo_df)


@pytest.mark.vcr(record_mode="none")
def test_get_ipo_calendar_400(mocker):
    attrs = {
        "status_code": 400,
        "json.return_value": {"error": "mock error message"},
    }

    mock_response = mocker.Mock(**attrs)

    mocker.patch(
        target="openbb_terminal.helper_funcs.requests.get",
        new=mocker.Mock(return_value=mock_response),
    )
    ipo_df = finnhub_model.get_ipo_calendar(
        start_date="2021-12-01",
        end_date="2021-12-02",
    )
    assert ipo_df.empty
