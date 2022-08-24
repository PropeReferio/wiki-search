from typing import Union
from urllib.parse import urlparse

from flask import Flask, request
from flask.wrappers import Response

from search import search_wikipedia

app = Flask(__name__)


@app.route("/")
def index() -> Union[str, Response]:
    """
    Get back a JSON of links returned by the user's search term.
    The search term is the subdomain.
    :return: str or Response
    """
    base_url = urlparse(request.base_url)
    if (
        base_url.netloc == "wiki-search.com:5000"
        or base_url.netloc == "www.wiki-search.com:5000"
    ):
        return (
            "Try searching for a wikipedia article by "
            "putting your search term in the subdomain."
        )
    else:
        search_term = base_url.netloc.split(".")[0]
        results = search_wikipedia(search_term)
        return results
