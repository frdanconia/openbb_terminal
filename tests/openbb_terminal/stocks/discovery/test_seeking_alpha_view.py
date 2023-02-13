# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.discovery import seeking_alpha_view


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
    }


@pytest.mark.vcr
@pytest.mark.record_stdout
def test_upcoming_earning_release_dates():
    seeking_alpha_view.upcoming_earning_release_dates(
        num_pages=1,
        limit=2,
        export="",
    )


@pytest.mark.vcr
@pytest.mark.record_stdout
def test_news():
    seeking_alpha_view.news(
        article_id=-1,
        limit=2,
        export="",
    )


@pytest.mark.vcr
@pytest.mark.record_stdout
def test_display_news():
    seeking_alpha_view.display_news(
        news_type="Crypto",
        limit=2,
        export="",
    )
