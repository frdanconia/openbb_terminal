# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest
import requests

# IMPORTATION INTERNAL
from openbb_terminal.stocks.fundamental_analysis import eclect_us_model


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
def test_get_filings_analysis(recorder):
    result = eclect_us_model.get_filings_analysis(symbol="PM")

    recorder.capture(result)


@pytest.mark.vcr(record_mode="none")
def test_get_filings_analysis_invalid(mocker):
    mock_response = requests.Response()
    mock_response.status_code = 400
    mocker.patch(
        target="openbb_terminal.helper_funcs.requests.get",
        new=mocker.Mock(return_value=mock_response),
    )

    result = eclect_us_model.get_filings_analysis(symbol="PM")
    assert result.empty
