# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import finviz.main_func
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.insider import finviz_model


@pytest.mark.vcr
def test_get_last_insider_activity(mocker, recorder):
    # REMOVE FINVIZ STOCK_PAGE CACHE
    mocker.patch.object(target=finviz.main_func, attribute="STOCK_PAGE", new={})

    result_df = finviz_model.get_last_insider_activity(symbol="PM")
    recorder.capture(result_df)
