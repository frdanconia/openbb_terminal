# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pandas as pd
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.cryptocurrency.due_diligence import coinbase_model


@pytest.mark.vcr
@pytest.mark.parametrize(
    "func, kwargs",
    [
        ("show_available_pairs_for_given_symbol", dict()),
        ("get_trading_pair_info", dict(symbol="ETH-USDT")),
        ("get_trades", dict(symbol="ETH-USDT", side="buy")),
        ("get_candles", dict(symbol="ETH-USDT")),
        ("get_product_stats", dict(symbol="ETH-USDT")),
    ],
)
def test_call_func(func, kwargs, recorder):
    result = getattr(coinbase_model, func)(**kwargs)

    if isinstance(result, tuple):
        recorder.capture_list(result)
    else:
        recorder.capture(result)


@pytest.mark.vcr
def test_get_order_book(recorder):
    result = coinbase_model.get_order_book(symbol="ETH-USDT")
    bids, asks, product_id, market_book = result
    bids = pd.DataFrame(data=bids)
    asks = pd.DataFrame(data=asks)

    recorder.capture_list([bids, asks, product_id, market_book])
