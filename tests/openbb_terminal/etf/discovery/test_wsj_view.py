# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

from openbb_terminal import helper_funcs

# IMPORTATION INTERNAL
from openbb_terminal.etf.discovery import wsj_view


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
    }


@pytest.mark.vcr()
@pytest.mark.record_stdout
@pytest.mark.parametrize(
    "sort_type",
    [
        "gainers",
        "decliners",
        "active",
    ],
)
def test_show_top_mover(sort_type, mocker):
    mocker.patch.object(
        target=helper_funcs.obbff, attribute="USE_TABULATE_DF", new=False
    )
    wsj_view.show_top_mover(sort_type, limit=5, export="")
