# IMPORTATION STANDARD
import os
from typing import List

# IMPORTATION THIRDPARTY
import pandas as pd
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.cryptocurrency.due_diligence import dd_controller

# pylint: disable=E1101
# pylint: disable=W0603
# pylint: disable=E1111

MESSARI_TIMESERIES_DF = pd.DataFrame()

TOKENTERMINAL_PROJECTS: List[str] = list()

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


@pytest.mark.vcr(record_mode="none")
@pytest.mark.parametrize(
    "queue, expected",
    [
        (["load", "help"], ["help"]),
        (["quit", "help"], ["help"]),
    ],
)
def test_menu_with_queue(expected, mocker, queue):
    path_controller = "openbb_terminal.cryptocurrency.due_diligence.dd_controller"

    # MOCK SWITCH
    mocker.patch(
        target=f"{path_controller}.DueDiligenceController.switch",
        return_value=["quit"],
    )
    # MOCK MESSARI_TIMESERIES_DF
    mocker.patch(
        target=f"{path_controller}.messari_model.get_available_timeseries",
        return_value=MESSARI_TIMESERIES_DF,
    )
    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_exchanges",
        return_value=["ABC"],
    )
    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_binance_currencies",
        return_value=["BITCOIN"],
    )
    result_menu = dd_controller.DueDiligenceController(queue=queue).menu()

    assert result_menu == expected


@pytest.mark.vcr(record_mode="none")
def test_menu_without_queue_completion(mocker):
    path_controller = "openbb_terminal.cryptocurrency.due_diligence.dd_controller"

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
    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_exchanges",
        return_value=["ABC"],
    )

    # DISABLE AUTO-COMPLETION : CONTROLLER.COMPLETER
    mocker.patch.object(
        target=dd_controller.obbff,
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
    # MOCK MESSARI_TIMESERIES_DF
    mocker.patch(
        target=f"{path_controller}.messari_model.get_available_timeseries",
        return_value=MESSARI_TIMESERIES_DF,
    )

    # MOCK TOKEN TERMINAL get_project_ids
    mocker.patch(
        target=f"{path_controller}.tokenterminal_model.get_project_ids",
        return_value=TOKENTERMINAL_PROJECTS,
    )
    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_binance_currencies",
        return_value=["BITCOIN"],
    )

    controller = dd_controller.DueDiligenceController(
        symbol="BTC",
        queue=None,
    )

    result_menu = controller.menu()

    assert result_menu == ["help"]


@pytest.mark.vcr(record_mode="none")
@pytest.mark.parametrize(
    "mock_input",
    ["help", "homee help", "home help", "mock"],
)
def test_menu_without_queue_sys_exit(mock_input, mocker):
    path_controller = "openbb_terminal.cryptocurrency.due_diligence.dd_controller"

    # DISABLE AUTO-COMPLETION
    mocker.patch.object(
        target=dd_controller.obbff,
        attribute="USE_PROMPT_TOOLKIT",
        new=False,
    )
    mocker.patch(
        target=f"{path_controller}.session",
        return_value=None,
    )

    # MOCK USER INPUT
    mocker.patch("builtins.input", return_value=mock_input)

    # MOCK MESSARI_TIMESERIES_DF
    mocker.patch(
        target=f"{path_controller}.messari_model.get_available_timeseries",
        return_value=MESSARI_TIMESERIES_DF,
    )
    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_exchanges",
        return_value=["ABC"],
    )
    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_binance_currencies",
        return_value=["BITCOIN"],
    )

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
        target=f"{path_controller}.DueDiligenceController.switch",
        new=mock_switch,
    )
    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_exchanges",
        return_value=["ABC"],
    )
    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_binance_currencies",
        return_value=["BITCOIN"],
    )

    result_menu = dd_controller.DueDiligenceController(queue=None).menu()

    assert result_menu == ["help"]


@pytest.mark.vcr(record_mode="none")
@pytest.mark.record_stdout
def test_print_help(mocker):
    path_controller = "openbb_terminal.cryptocurrency.due_diligence.dd_controller"

    # MOCK MESSARI_TIMESERIES_DF
    mocker.patch(
        target=f"{path_controller}.messari_model.get_available_timeseries",
        return_value=MESSARI_TIMESERIES_DF,
    )
    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_exchanges",
        return_value=["ABC"],
    )
    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_binance_currencies",
        return_value=["BITCOIN"],
    )
    controller = dd_controller.DueDiligenceController(queue=None)
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
            ["quit", "quit", "reset", "crypto", "dd"],
        ),
    ],
)
def test_switch(an_input, expected_queue, mocker):
    path_controller = "openbb_terminal.cryptocurrency.due_diligence.dd_controller"

    # MOCK MESSARI_TIMESERIES_DF
    mocker.patch(
        target=f"{path_controller}.messari_model.get_available_timeseries",
        return_value=MESSARI_TIMESERIES_DF,
    )
    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_exchanges",
        return_value=["ABC"],
    )

    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_binance_currencies",
        return_value=["BITCOIN"],
    )
    controller = dd_controller.DueDiligenceController(queue=None)
    queue = controller.switch(an_input=an_input)

    assert queue == expected_queue


@pytest.mark.vcr(record_mode="none")
def test_call_cls(mocker):
    mocker.patch("os.system")

    path_controller = "openbb_terminal.cryptocurrency.due_diligence.dd_controller"

    # MOCK MESSARI_TIMESERIES_DF
    mocker.patch(
        target=f"{path_controller}.messari_model.get_available_timeseries",
        return_value=MESSARI_TIMESERIES_DF,
    )
    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_exchanges",
        return_value=["ABC"],
    )

    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_binance_currencies",
        return_value=["BITCOIN"],
    )
    controller = dd_controller.DueDiligenceController(queue=None)
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
            ["quit", "quit", "quit"],
        ),
        ("call_exit", ["help"], ["quit", "quit", "quit", "help"]),
        ("call_home", [], ["quit", "quit"]),
        ("call_help", [], []),
        ("call_quit", [], ["quit"]),
        ("call_quit", ["help"], ["quit", "help"]),
        (
            "call_reset",
            [],
            ["quit", "quit", "reset", "crypto", "dd"],
        ),
        (
            "call_reset",
            ["help"],
            ["quit", "quit", "reset", "crypto", "dd", "help"],
        ),
    ],
)
def test_call_func_expect_queue(expected_queue, func, queue, mocker):
    path_controller = "openbb_terminal.cryptocurrency.due_diligence.dd_controller"

    # MOCK MESSARI_TIMESERIES_DF
    mocker.patch(
        target=f"{path_controller}.messari_model.get_available_timeseries",
        return_value=MESSARI_TIMESERIES_DF,
    )
    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_binance_currencies",
        return_value=["BITCOIN"],
    )
    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_exchanges", return_value=["BITCOIN"]
    )
    controller = dd_controller.DueDiligenceController(queue=queue)
    result = getattr(controller, func)([])

    assert result is None
    assert controller.queue == expected_queue


@pytest.mark.vcr(record_mode="none")
@pytest.mark.parametrize(
    "tested_func, other_args, mocked_func, called_args, called_kwargs",
    [
        (
            "call_nonzero",
            [],
            "glassnode_view.display_non_zero_addresses",
            [],
            dict(),
        ),
        (
            "call_active",
            [],
            "glassnode_view.display_active_addresses",
            [],
            dict(),
        ),
        (
            "call_change",
            ["binance"],
            "glassnode_view.display_exchange_net_position_change",
            [],
            dict(),
        ),
        (
            "call_eb",
            [],
            "glassnode_view.display_exchange_balances",
            [],
            dict(),
        ),
        (
            "call_fundrate",
            [],
            "coinglass_view.display_funding_rate",
            [],
            dict(),
        ),
        (
            "call_liquidations",
            [],
            "coinglass_view.display_liquidations",
            [],
            dict(),
        ),
        (
            "call_oi",
            [],
            "coinglass_view.display_open_interest",
            [],
            dict(),
        ),
        (
            "call_info",
            [],
            "pycoingecko_view.display_info",
            [],
            dict(),
        ),
        (
            "call_market",
            [],
            "pycoingecko_view.display_market",
            [],
            dict(),
        ),
        (
            "call_web",
            [],
            "pycoingecko_view.display_web",
            [],
            dict(),
        ),
        (
            "call_dev",
            [],
            "pycoingecko_view.display_dev",
            [],
            dict(),
        ),
        (
            "call_ath",
            [],
            "pycoingecko_view.display_ath",
            [],
            dict(),
        ),
        (
            "call_atl",
            [],
            "pycoingecko_view.display_atl",
            [],
            dict(),
        ),
        (
            "call_score",
            [],
            "pycoingecko_view.display_score",
            [],
            dict(),
        ),
        (
            "call_bc",
            [],
            "pycoingecko_view.display_bc",
            [],
            dict(),
        ),
        (
            "call_ob",
            [],
            "ccxt_view.display_order_book",
            [],
            dict(),
        ),
        (
            "call_trades",
            [],
            "ccxt_view.display_trades",
            [],
            dict(),
        ),
        (
            "call_balance",
            [],
            "binance_view.display_balance",
            [],
            dict(),
        ),
        (
            "call_stats",
            [],
            "coinbase_view.display_stats",
            [],
            dict(),
        ),
        (
            "call_ps",
            [],
            "coinpaprika_view.display_price_supply",
            [],
            dict(),
        ),
        (
            "call_basic",
            [],
            "coinpaprika_view.display_basic",
            [],
            dict(),
        ),
        (
            "call_mkt",
            [],
            "coinpaprika_view.display_markets",
            [],
            dict(),
        ),
        (
            "call_ex",
            [],
            "coinpaprika_view.display_exchanges",
            [],
            dict(),
        ),
        (
            "call_events",
            [],
            "coinpaprika_view.display_events",
            [],
            dict(),
        ),
        (
            "call_twitter",
            [],
            "coinpaprika_view.display_twitter",
            [],
            dict(),
        ),
    ],
)
def test_call_func(
    tested_func, mocked_func, other_args, called_args, called_kwargs, mocker
):
    path_controller = "openbb_terminal.cryptocurrency.due_diligence.dd_controller"

    # MOCK GET_COINGECKO_ID
    mocker.patch(
        target=f"{path_controller}.cryptocurrency_helpers.get_coingecko_id",
        return_value=True,
    )

    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_exchanges",
        return_value=["ABC"],
    )
    mocker.patch(
        target=f"{path_controller}.ccxt_model.get_binance_currencies",
        return_value=["BITCOIN"],
    )

    # MOCK SHOW_AVAILABLE_PAIRS_FOR_GIVEN_SYMBOL
    mocker.patch(
        target=f"{path_controller}.binance_model.show_available_pairs_for_given_symbol",
        return_value=BINANCE_SHOW_AVAILABLE_PAIRS_OF_GIVEN_SYMBOL,
    )

    # MOCK SHOW_AVAILABLE_PAIRS_FOR_GIVEN_SYMBOL
    mocker.patch(
        target=f"{path_controller}.coinbase_model.show_available_pairs_for_given_symbol",
        return_value=COINBASE_SHOW_AVAILABLE_PAIRS_OF_GIVEN_SYMBOL,
    )

    # MOCK MESSARI_TIMESERIES_DF
    mocker.patch(
        target=f"{path_controller}.messari_model.get_available_timeseries",
        return_value=MESSARI_TIMESERIES_DF,
    )

    if mocked_func:
        mock = mocker.Mock()
        mocker.patch(
            target=f"{path_controller}.{mocked_func}",
            new=mock,
        )

        controller = dd_controller.DueDiligenceController()
        controller.coin_map_df = COIN_MAP_DF
        controller.current_coin = CURRENT_COIN
        controller.symbol = SYMBOL
        getattr(controller, tested_func)(other_args)

        if called_args or called_kwargs:
            mock.assert_called_once_with(*called_args, **called_kwargs)
        else:
            mock.assert_called_once()
    else:
        controller = dd_controller.DueDiligenceController()
        controller.coin_map_df = COIN_MAP_DF
        controller.current_coin = CURRENT_COIN
        controller.symbol = SYMBOL
        getattr(controller, tested_func)(other_args)
