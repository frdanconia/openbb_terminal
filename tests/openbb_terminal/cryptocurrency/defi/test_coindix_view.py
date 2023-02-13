# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pandas as pd
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.cryptocurrency.defi import coindix_view


@pytest.mark.vcr
@pytest.mark.record_stdout
def test_display_defi_vaults(mocker):
    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.cryptocurrency.defi.coindix_view.export_data")

    coindix_view.display_defi_vaults(
        chain=None,
        protocol=None,
        kind=None,
        limit=None,
        sortby="apy",
        ascend=False,
        link=True,
        export="",
    )


@pytest.mark.vcr(record_mode="none")
@pytest.mark.record_stdout
def test_display_defi_vaults_empty_df(mocker):
    # MOCK GET_DEFI_VAULTS
    mocker.patch(
        target="openbb_terminal.cryptocurrency.defi.coindix_view.coindix_model.get_defi_vaults",
        return_value=pd.DataFrame(),
    )

    coindix_view.display_defi_vaults(
        chain=None,
        protocol=None,
        kind=None,
        limit=None,
        sortby="apy",
        ascend=False,
        link=True,
        export="",
    )
