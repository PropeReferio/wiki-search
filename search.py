from dataclasses import dataclass
from json import loads

import requests
from flask import jsonify
from tenacity import retry, stop_after_attempt

WIKI_OPEN_SEARCH_URL = (
    "https://en.wikipedia.org/w/api.php?"
    "action=opensearch&format=json&list=search&search="
)
WIKI_QUERY_REDIRECTS_URL = (
    "https://en.wikipedia.org/w/api.php"
    "?action=query&prop=redirects&format=json&titles="
)


@dataclass
class OpenSearchResult:
    term: str
    titles: list[str]
    links: list[str]

    @retry(stop=stop_after_attempt(3))
    def is_exact_match(self):
        """
        Determines if search term would go straight to a wikipedia
        article, rather than a list of results.
        :return: bool, str
        """
        for i, title in enumerate(self.titles):
            if self.term.lower() == title.lower():
                return True, self.links[i]
            try:
                resp = requests.get(f"{WIKI_QUERY_REDIRECTS_URL}{title}")
            except Exception as e:
                raise Exception(f"There was a problem while checking for redirects: {e}")
            resp_json = loads(resp.text)
            page_id = list(resp_json["query"]["pages"].keys())[0]
            page = resp_json["query"]["pages"][page_id]
            if "redirects" in page:
                redirect_titles = [
                    item["title"].lower()
                    for item in resp_json["query"]["pages"][page_id]["redirects"]
                ]
                if self.term in redirect_titles:
                    return True, self.links[i]
            elif page["title"].lower() == self.term:
                return True, self.links[i]
        return False, None


@retry(stop=stop_after_attempt(3))
def search_wikipedia(term):
    """
    Searches the opensearch endpoint of the wikipedia API,
    and returns the results as json.
    :param term:
    :return:
    """
    try:
        resp = requests.get(f"{WIKI_OPEN_SEARCH_URL}{term}")
    except Exception as e:
        raise Exception(f"There was a problem while searching wikipedia: {e}")
    resp_json = loads(resp.text)
    result = OpenSearchResult(term, resp_json[1], resp_json[3])
    is_match, link = result.is_exact_match()
    if is_match:
        return jsonify({"links": link})
    else:
        return jsonify({"links": result.links})
