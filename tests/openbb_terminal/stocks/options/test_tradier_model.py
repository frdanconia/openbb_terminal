# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest
import requests

# IMPORTATION INTERNAL
from openbb_terminal.stocks.options import tradier_model


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("Authorization", "MOCK_TOKEN")],
    }


@pytest.mark.vcr
def test_get_historical_options(recorder):
    result_df = tradier_model.get_historical_options(
        symbol="AAPL",
        expiry="2025-01-17",
        strike=90.0,
        put=True,
        chain_id="",
    )
    recorder.capture(result_df)


@pytest.mark.vcr(record_mode="none")
def test_get_historical_options_invalid_status(mocker):
    mock_response = requests.Response()
    mock_response.status_code = 400
    mocker.patch(
        target="openbb_terminal.helper_funcs.requests.get",
        new=mocker.Mock(return_value=mock_response),
    )

    result_df = tradier_model.get_historical_options(
        symbol="AAPL",
        expiry="2025-01-17",
        strike=90.0,
        put=True,
        chain_id="MOCK_CHAIN_ID",
    )

    assert result_df.empty


@pytest.mark.vcr(record_mode="none")
def test_get_historical_options_no_data(mocker):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mocker.patch.object(
        target=mock_response,
        attribute="json",
        return_value={"history": None},
    )
    mocker.patch(
        target="openbb_terminal.helper_funcs.requests.get",
        new=mocker.Mock(return_value=mock_response),
    )

    result_df = tradier_model.get_historical_options(
        symbol="AAPL",
        expiry="2022-02-25",
        strike=90.0,
        put=True,
        chain_id="MOCK_CHAIN_ID",
    )

    assert result_df.empty


@pytest.mark.vcr
def test_option_expirations(recorder):
    result_list = tradier_model.option_expirations(symbol="AAPL")
    recorder.capture(result_list)


@pytest.mark.vcr
def test_option_expirations_json_error(mocker):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mocker.patch.object(
        target=mock_response,
        attribute="json",
        side_effect=TypeError(),
    )
    mocker.patch(
        target="openbb_terminal.helper_funcs.requests.get",
        new=mocker.Mock(return_value=mock_response),
    )

    result_list = tradier_model.option_expirations(symbol="AAPL")

    assert result_list == []


@pytest.mark.vcr(record_mode="none")
def test_option_expirations_invalid_status(mocker):
    mock_response = requests.Response()
    mock_response.status_code = 400
    mocker.patch(
        target="openbb_terminal.helper_funcs.requests.get",
        new=mocker.Mock(return_value=mock_response),
    )

    result_list = tradier_model.option_expirations(symbol="AAPL")

    assert result_list == []


@pytest.mark.vcr
def test_get_option_chains(recorder):
    chain = tradier_model.get_option_chain(symbol="AAPL", expiry="2025-01-17")
    recorder.capture(chain)


@pytest.mark.vcr(record_mode="none")
def test_get_option_chains_invalid_status(mocker):
    mock_response = requests.Response()
    mock_response.status_code = 400
    mocker.patch(
        target="openbb_terminal.helper_funcs.requests.get",
        new=mocker.Mock(return_value=mock_response),
    )

    result_df = tradier_model.get_option_chain(symbol="AAPL", expiry="2025-01-17")

    assert result_df.empty


@pytest.mark.vcr
def test_last_price(recorder):
    result = tradier_model.get_last_price(symbol="AAPL")
    recorder.capture(result)


@pytest.mark.vcr(record_mode="none")
def test_get_historical_greeks_invalid_status(mocker):
    mock_response = requests.Response()
    mock_response.status_code = 400
    mocker.patch(
        target="openbb_terminal.helper_funcs.requests.get",
        new=mocker.Mock(return_value=mock_response),
    )

    result = tradier_model.get_last_price(symbol="AAPL")

    assert result is None
