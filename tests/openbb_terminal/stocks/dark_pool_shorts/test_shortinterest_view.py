# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.dark_pool_shorts import shortinterest_view


@pytest.mark.vcr
@pytest.mark.record_stdout
def test_high_short_interest():
    shortinterest_view.high_short_interest(
        limit=2,
        export="",
        sheet_name=None,
    )
