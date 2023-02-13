# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.comparison_analysis import finnhub_model


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_query_parameters": [
            ("token", "MOCK_TOKEN"),
        ],
    }


@pytest.mark.vcr
def test_get_similar_companies(recorder):
    result = finnhub_model.get_similar_companies(symbol="TSLA")

    recorder.capture(result)


@pytest.mark.vcr(record_mode="none")
def test_get_similar_companies_invalid_status(mocker, recorder):
    attrs = {
        "status_code": 400,
        "json.return_value": {"error": "mock error message"},
    }

    mock_response = mocker.Mock(**attrs)

    mocker.patch(
        target="openbb_terminal.helper_funcs.requests.get",
        new=mocker.Mock(return_value=mock_response),
    )
    result = finnhub_model.get_similar_companies(symbol="TSLA")

    recorder.capture(result)
