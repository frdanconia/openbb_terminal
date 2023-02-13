# IMPORTATION STANDARD
import os

# IMPORTATION THIRDPARTY
import pandas as pd
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.cryptocurrency import crypto_controller

# pylint: disable=E1101
# pylint: disable=W0603
# pylint: disable=E1111

COIN_MAP_DF = pd.Series(
    data={
        "CoinGecko": "bitcoin",
        "CoinPaprika": "btc-bitcoin",
        "Binance": "BTC",
        "Coinbase": "BTC",
    }
)
CURRENT_COIN = "bitcoin"
SYMBOL = "BTC"
BINANCE_SHOW_AVAILABLE_PAIRS_OF_GIVEN_SYMBOL = (
    "BTC",
    [
        "USDT",
        "TUSD",
        "USDC",
        "BUSD",
        "NGN",
        "RUB",
        "TRY",
        "EUR",
        "GBP",
        "UAH",
        "BIDR",
        "AUD",
        "DAI",
        "BRL",
        "USDP",
    ],
)
COINBASE_SHOW_AVAILABLE_PAIRS_OF_GIVEN_SYMBOL = (
    "BTC",
    ["GBP", "USD", "EUR", "USDC", "UST", "USDT"],
)


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_query_parameters": [
            ("days", "MOCK_DAYS"),
        ]
    }


@pytest.mark.vcr(record_mode="none")
@pytest.mark.parametrize(
    "queue, expected",
    [
        (["load", "help"], ["help"]),
        (["quit", "help"], ["help"]),
    ],
)
def test_menu_with_queue(expected, mocker, queue):
    path_controller = "openbb_terminal.cryptocurrency.crypto_controller"

    # MOCK SWITCH
    mocker.patch(
        target=f"{path_controller}.CryptoController.switch",
        return_value=["quit"],
    )
    result_menu = crypto_controller.CryptoController(queue=queue).menu()

    assert result_menu == expected


@pytest.mark.vcr(record_mode="none")
def test_menu_without_queue_completion(mocker):
    path_controller = "openbb_terminal.cryptocurrency.crypto_controller"

    # ENABLE AUTO-COMPLETION : HELPER_FUNCS.MENU
    mocker.patch(
        target="openbb_terminal.feature_flags.USE_PROMPT_TOOLKIT",
        new=True,
    )
    mocker.patch(
        target="openbb_terminal.parent_classes.session",
    )
    mocker.patch(
        target="openbb_terminal.parent_classes.session.prompt",
        return_value="quit",
    )

    # DISABLE AUTO-COMPLETION : CONTROLLER.COMPLETER
    mocker.patch.object(
        target=crypto_controller.obbff,
        attribute="USE_PROMPT_TOOLKIT",
        new=True,
    )
    mocker.patch(
        target=f"{path_controller}.session",
    )
    mocker.patch(
        target=f"{path_controller}.session.prompt",
        return_value="quit",
    )

    result_menu = crypto_controller.CryptoController(queue=None).menu()

    assert result_menu == ["help"]


@pytest.mark.vcr(record_mode="none")
@pytest.mark.parametrize(
    "mock_input",
    ["help", "homee help", "home help", "mock"],
)
def test_menu_without_queue_sys_exit(mock_input, mocker):
    path_controller = "openbb_terminal.cryptocurrency.crypto_controller"

    # DISABLE AUTO-COMPLETION
    mocker.patch.object(
        target=crypto_controller.obbff,
        attribute="USE_PROMPT_TOOLKIT",
        new=False,
    )
    mocker.patch(
        target=f"{path_controller}.session",
        return_value=None,
    )

    # MOCK USER INPUT
    mocker.patch("builtins.input", return_value=mock_input)

    # MOCK SWITCH
    class SystemExitSideEffect:
        def __init__(self):
            self.first_call = True

        def __call__(self, *args, **kwargs):
            if self.first_call:
                self.first_call = False
                raise SystemExit()
            return ["quit"]

    mock_switch = mocker.Mock(side_effect=SystemExitSideEffect())
    mocker.patch(
        target=f"{path_controller}.CryptoController.switch",
        new=mock_switch,
    )

    result_menu = crypto_controller.CryptoController(queue=None).menu()

    assert result_menu == ["help"]


@pytest.mark.vcr(record_mode="none")
@pytest.mark.record_stdout
def test_print_help():
    controller = crypto_controller.CryptoController(queue=None)
    controller.print_help()


@pytest.mark.vcr(record_mode="none")
@pytest.mark.parametrize(
    "an_input, expected_queue",
    [
        ("", []),
        ("/help", ["home", "help"]),
        ("help/help", ["help", "help"]),
        ("q", ["quit"]),
        ("h", []),
        (
            "r",
            ["quit", "reset", "crypto"],
        ),
    ],
)
def test_switch(an_input, expected_queue):
    controller = crypto_controller.CryptoController(queue=None)
    queue = controller.switch(an_input=an_input)

    assert queue == expected_queue


@pytest.mark.vcr(record_mode="none")
def test_call_cls(mocker):
    mocker.patch("os.system")

    controller = crypto_controller.CryptoController(queue=None)
    controller.call_cls([])

    assert controller.queue == []
    os.system.assert_called_once_with("cls||clear")


@pytest.mark.vcr(record_mode="none")
@pytest.mark.parametrize(
    "func, queue, expected_queue",
    [
        (
            "call_exit",
            [],
            ["quit", "quit"],
        ),
        ("call_exit", ["help"], ["quit", "quit", "help"]),
        ("call_home", [], ["quit"]),
        ("call_help", [], []),
        ("call_quit", [], ["quit"]),
        ("call_quit", ["help"], ["quit", "help"]),
        (
            "call_reset",
            [],
            ["quit", "reset", "crypto"],
        ),
        (
            "call_reset",
            ["help"],
            ["quit", "reset", "crypto", "help"],
        ),
    ],
)
def test_call_func_expect_queue(expected_queue, func, queue):
    controller = crypto_controller.CryptoController(queue=queue)
    result = getattr(controller, func)([])

    assert result is None
    assert controller.queue == expected_queue


@pytest.mark.vcr(record_mode="none")
@pytest.mark.parametrize(
    "tested_func, other_args, mocked_func, called_args, called_kwargs",
    [
        (
            "call_prt",
            ["eth"],
            "pycoingecko_view.display_coin_potential_returns",
            [],
            dict(),
        ),
        (
            "call_disc",
            [],
            "CryptoController.load_class",
            [],
            dict(),
        ),
        (
            "call_ov",
            [],
            "CryptoController.load_class",
            [],
            dict(),
        ),
        (
            "call_defi",
            [],
            "CryptoController.load_class",
            [],
            dict(),
        ),
        (
            "call_headlines",
            [],
            "finbrain_crypto_view.display_crypto_sentiment_analysis",
            [],
            dict(),
        ),
        (
            "call_dd",
            [],
            "CryptoController.load_class",
            [],
            dict(),
        ),
        (
            "call_onchain",
            [],
            "CryptoController.load_class",
            [],
            dict(),
        ),
        (
            "call_nft",
            [],
            "CryptoController.load_class",
            [],
            dict(),
        ),
        (
            "call_tools",
            [],
            "CryptoController.load_class",
            [],
            dict(),
        ),
    ],
)
def test_call_func(
    tested_func, mocked_func, other_args, called_args, called_kwargs, mocker
):
    path_controller = "openbb_terminal.cryptocurrency.crypto_controller"

    # MOCK GET_COINGECKO_ID
    mocker.patch(
        target=f"{path_controller}.cryptocurrency_helpers.get_coingecko_id",
        return_value=True,
    )

    if mocked_func:
        mock = mocker.Mock()
        mocker.patch(
            target=f"{path_controller}.{mocked_func}",
            new=mock,
        )

        controller = crypto_controller.CryptoController(queue=None)
        controller.symbol = SYMBOL
        controller.source = "bin"
        getattr(controller, tested_func)(other_args)

        if called_args or called_kwargs:
            mock.assert_called_once_with(*called_args, **called_kwargs)
        else:
            mock.assert_called_once()
    else:
        controller = crypto_controller.CryptoController(queue=None)
        controller.symbol = SYMBOL
        controller.source = "bin"
        getattr(controller, tested_func)(other_args)


@pytest.mark.vcr(record_mode="none")
@pytest.mark.parametrize(
    "tested_func",
    [
        "call_prt",
        "call_candle",
        "call_ta",
        "call_dd",
    ],
)
def test_call_func_no_current_coin(tested_func):
    controller = crypto_controller.CryptoController(queue=None)
    controller.symbol = None
    getattr(controller, tested_func)([])
