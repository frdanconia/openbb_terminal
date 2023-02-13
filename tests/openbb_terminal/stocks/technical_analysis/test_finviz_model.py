# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.technical_analysis import finviz_model


@pytest.mark.vcr
def test_get_finviz_image():
    result = finviz_model.get_finviz_image(symbol="PM")
    assert isinstance(result, bytes)
