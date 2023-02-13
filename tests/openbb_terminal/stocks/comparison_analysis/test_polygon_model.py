# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest
import requests

# IMPORTATION INTERNAL
from openbb_terminal.stocks.comparison_analysis import polygon_model


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_query_parameters": [
            ("apiKey", "MOCK_APIKEY"),
        ],
    }


@pytest.mark.vcr
def test_get_financial_comparisons(recorder):
    result = polygon_model.get_similar_companies(
        symbol="TSLA",
        us_only=True,
    )

    recorder.capture(result)


@pytest.mark.vcr(record_mode="none")
def test_get_similar_companies_invalid_status(mocker, recorder):
    mock_response = requests.Response()
    mock_response.status_code = 400
    # pylint: disable=protected-access
    mock_response._content = b"""{"error":"MOCK_ERROR"}"""
    mocker.patch(
        target="openbb_terminal.helper_funcs.requests.get",
        new=mocker.Mock(return_value=mock_response),
    )
    result = polygon_model.get_similar_companies(
        symbol="TSLA",
        us_only=True,
    )

    recorder.capture(result)
