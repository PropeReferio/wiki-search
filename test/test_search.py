from unittest.mock import patch

import pytest

from app import app
from search import search_wikipedia


@patch("search.OpenSearchResult.is_exact_match")
@patch("search.requests.get")
@pytest.mark.parametrize("search_term", ["boof", "ital", "repr"])
def test_search_wikipedia(
    mock_get,
    mock_is_exact_match,
    boof_open_search,
    ital_open_search,
    repr_open_search,
    search_term,
):
    match search_term:
        case "boof":
            mock_get.return_value.text = boof_open_search
            mock_is_exact_match.return_value = (
                True,
                "https://en.wikipedia.org/wiki/Boof",
            )
        case "ital":
            mock_get.return_value.text = ital_open_search
            mock_is_exact_match.return_value = (
                True,
                "https://en.wikipedia.org/wiki/Ital",
            )
        case "repr":
            mock_get.return_value.text = repr_open_search
            mock_is_exact_match.return_value = (False, None)
    with app.app_context():
        final_json = search_wikipedia(search_term)
    match search_term:
        # Testing that different terms return only one, or
        # ten results (exact match or not)
        case "boof":
            assert len(final_json.json["links"]) == 1
        case "ital":
            assert len(final_json.json["links"]) == 1
        case "repr":
            assert len(final_json.json["links"]) == 10
