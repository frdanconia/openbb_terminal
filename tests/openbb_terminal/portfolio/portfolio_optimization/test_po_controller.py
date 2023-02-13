# IMPORTATION STANDARD
import os

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
try:
    from openbb_terminal.portfolio.portfolio_optimization import po_controller
except ImportError:
    pytest.skip(allow_module_level=True)

# pylint: disable=E1101
# pylint: disable=W0603
# pylint: disable=E1111


def test_update_runtime_choices(mocker):
    mocker.patch(
        "openbb_terminal.portfolio.portfolio_optimization.po_controller.session", True
    )
    mocker.patch("openbb_terminal.feature_flags.USE_PROMPT_TOOLKIT", True)
    cont = po_controller.PortfolioOptimizationController(
        tickers=["TSLA", "AAPL"], portfolios={"port": 1}, categories={"cat": 1}
    )
    cont.update_runtime_choices()


def test_custom_reset():
    cont = po_controller.PortfolioOptimizationController()
    cont.current_portfolio = {"po": 1}
    cont.current_file = "somefile.csv"
    command = cont.custom_reset()
    assert command[2][:4] == "load"
    assert command[3][:4] == "file"


@pytest.mark.vcr(record_mode="none")
@pytest.mark.parametrize(
    "queue, expected",
    [
        (["load", "help"], ["help"]),
        (["quit", "help"], ["help"]),
    ],
)
def test_menu_with_queue(expected, mocker, queue):
    path_controller = "openbb_terminal.portfolio.portfolio_optimization.po_controller"

    # MOCK SWITCH
    mocker.patch(
        target=f"{path_controller}.PortfolioOptimizationController.switch",
        return_value=["quit"],
    )
    result_menu = po_controller.PortfolioOptimizationController(queue=queue).menu()

    assert result_menu == expected


@pytest.mark.vcr(record_mode="none")
def test_menu_without_queue_completion(mocker):
    path_controller = "openbb_terminal.portfolio.portfolio_optimization.po_controller"

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
        target=po_controller.obbff,
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

    result_menu = po_controller.PortfolioOptimizationController(queue=None).menu()

    assert result_menu == ["help"]


@pytest.mark.vcr(record_mode="none")
@pytest.mark.parametrize(
    "mock_input",
    ["help", "homee help", "home help", "mock"],
)
def test_menu_without_queue_sys_exit(mock_input, mocker):
    path_controller = "openbb_terminal.portfolio.portfolio_optimization.po_controller"

    # DISABLE AUTO-COMPLETION
    mocker.patch.object(
        target=po_controller.obbff,
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
        target=f"{path_controller}.PortfolioOptimizationController.switch",
        new=mock_switch,
    )

    result_menu = po_controller.PortfolioOptimizationController(queue=None).menu()

    assert result_menu == ["help"]


@pytest.mark.vcr(record_mode="none")
@pytest.mark.record_stdout
def test_print_help():
    controller = po_controller.PortfolioOptimizationController(queue=None)
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
            ["quit", "quit", "reset", "portfolio", "po"],
        ),
    ],
)
def test_switch(an_input, expected_queue):
    controller = po_controller.PortfolioOptimizationController(queue=None)
    queue = controller.switch(an_input=an_input)

    assert queue == expected_queue


@pytest.mark.vcr(record_mode="none")
def test_call_cls(mocker):
    mocker.patch("os.system")

    controller = po_controller.PortfolioOptimizationController(queue=None)
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
            ["quit", "quit", "reset", "portfolio", "po"],
        ),
        (
            "call_reset",
            ["help"],
            ["quit", "quit", "reset", "portfolio", "po", "help"],
        ),
    ],
)
def test_call_func_expect_queue(expected_queue, func, queue):
    controller = po_controller.PortfolioOptimizationController(queue=queue)
    result = getattr(controller, func)([])

    assert result is None
    assert controller.queue == expected_queue


@pytest.mark.vcr(record_mode="none")
@pytest.mark.parametrize(
    "tested_func, other_args, mocked_func, called_args, called_kwargs",
    [
        (
            "call_equal",
            [],
            "optimizer_view.display_equal_weight",
            [],
            dict(),
        ),
        (
            "call_mktcap",
            [],
            "optimizer_view.display_property_weighting",
            [],
            dict(),
        ),
        (
            "call_maxsharpe",
            [],
            "optimizer_view.display_max_sharpe",
            [],
            dict(),
        ),
        (
            "call_minrisk",
            [],
            "optimizer_view.display_min_risk",
            [],
            dict(),
        ),
        (
            "call_ef",
            [],
            "optimizer_view.display_ef",
            [],
            dict(),
        ),
        (
            "call_file",
            ["-f=hello"],
            "",
            [],
            dict(),
        ),
        (
            "call_show",
            ["-ct=ASSET_CLASS"],
            "",
            [],
            dict(),
        ),
        (
            "call_maxutil",
            [],
            "optimizer_view.display_max_util",
            [],
            dict(),
        ),
        (
            "call_maxret",
            [],
            "optimizer_view.display_max_ret",
            [],
            dict(),
        ),
        (
            "call_maxdiv",
            [],
            "optimizer_view.display_max_div",
            [],
            dict(),
        ),
        (
            "call_maxdecorr",
            [],
            "optimizer_view.display_max_decorr",
            [],
            dict(),
        ),
        (
            "call_blacklitterman",
            [],
            "optimizer_view.display_black_litterman",
            [],
            dict(),
        ),
        (
            "call_riskparity",
            [],
            "optimizer_view.display_risk_parity",
            [],
            dict(),
        ),
        (
            "call_relriskparity",
            [],
            "optimizer_view.display_rel_risk_parity",
            [],
            dict(),
        ),
        (
            "call_hrp",
            [],
            "optimizer_view.display_hrp",
            [],
            dict(),
        ),
        (
            "call_herc",
            [],
            "optimizer_view.display_herc",
            [],
            dict(),
        ),
        (
            "call_nco",
            [],
            "optimizer_view.display_nco",
            [],
            dict(),
        ),
        (
            "call_load",
            [],
            "",
            [],
            dict(),
        ),
        (
            "call_plot",
            ["-pf=[]"],
            "",
            [],
            dict(),
        ),
    ],
)
def test_call_func(
    tested_func, mocked_func, other_args, called_args, called_kwargs, mocker
):
    path_controller = "openbb_terminal.portfolio.portfolio_optimization.po_controller"

    if mocked_func:
        mock = mocker.Mock()
        mocker.patch(
            target=f"{path_controller}.{mocked_func}",
            new=mock,
        )

        controller = po_controller.PortfolioOptimizationController(queue=None)
        controller.tickers = ["AAPL", "MSFT"]

        getattr(controller, tested_func)(other_args)

        if called_args or called_kwargs:
            mock.assert_called_once_with(*called_args, **called_kwargs)
        else:
            mock.assert_called_once()
    else:
        controller = po_controller.PortfolioOptimizationController(queue=None)

        getattr(controller, tested_func)(other_args)
