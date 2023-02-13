# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.cryptocurrency.defi import substack_view


@pytest.mark.vcr
@pytest.mark.record_stdout
def test_display_newsletters(mocker):
    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.cryptocurrency.defi.substack_view.export_data")

    # MOCK LEN
    mocker.patch(
        target="openbb_terminal.cryptocurrency.defi.substack_model.len",
        return_value=1,
    )

    substack_view.display_newsletters(limit=None, export="")
