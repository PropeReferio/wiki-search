from pytest import fixture


@fixture
def boof_open_search():
    boof_open_search = '["boof", ["Boof", "Boof Bonser", "Boofzheim", "Boof (Neighbours)", "Boofen", "Boof Pack", "Boofhead Catfish", "Boo FF", "Boo (film)", "Boo FK"], ["", "", "", "", "", "", "", "", "", ""], ["https://en.wikipedia.org/wiki/Boof", "https://en.wikipedia.org/wiki/Boof_Bonser", "https://en.wikipedia.org/wiki/Boofzheim", "https://en.wikipedia.org/wiki/Boof_(Neighbours)", "https://en.wikipedia.org/wiki/Boofen", "https://en.wikipedia.org/wiki/Boof_Pack", "https://en.wikipedia.org/wiki/Boofhead_Catfish", "https://en.wikipedia.org/wiki/Boo_FF", "https://en.wikipedia.org/wiki/Boo_(film)", "https://en.wikipedia.org/wiki/Boo_FK"]]'
    return boof_open_search


@fixture
def ital_open_search():
    ital_open_search = '["ital", ["Ital", "Italy", "Italian language", "Italy national football team", "Italian cuisine", "Italian Americans", "Italian fascism", "Italians", "Italian Wars", "Italian Social Republic"], ["", "", "", "", "", "", "", "", "", ""], ["https://en.wikipedia.org/wiki/Ital", "https://en.wikipedia.org/wiki/Italy", "https://en.wikipedia.org/wiki/Italian_language", "https://en.wikipedia.org/wiki/Italy_national_football_team", "https://en.wikipedia.org/wiki/Italian_cuisine", "https://en.wikipedia.org/wiki/Italian_Americans", "https://en.wikipedia.org/wiki/Italian_fascism", "https://en.wikipedia.org/wiki/Italians", "https://en.wikipedia.org/wiki/Italian_Wars", "https://en.wikipedia.org/wiki/Italian_Social_Republic"]]'
    return ital_open_search


@fixture
def repr_open_search():
    repr_open_search = '["repr", ["Representational state transfer", "Reproduction", "Reproductive rights", "Reproductive system", "Reproductive isolation", "Representation theory", "Representative matches in Australian rules football", "Repressed memory", "Reproductive justice", "Representation theory of the Lorentz group"], ["", "", "", "", "", "", "", "", "", ""], ["https://en.wikipedia.org/wiki/Representational_state_transfer", "https://en.wikipedia.org/wiki/Reproduction", "https://en.wikipedia.org/wiki/Reproductive_rights", "https://en.wikipedia.org/wiki/Reproductive_system", "https://en.wikipedia.org/wiki/Reproductive_isolation", "https://en.wikipedia.org/wiki/Representation_theory", "https://en.wikipedia.org/wiki/Representative_matches_in_Australian_rules_football", "https://en.wikipedia.org/wiki/Repressed_memory", "https://en.wikipedia.org/wiki/Reproductive_justice", "https://en.wikipedia.org/wiki/Representation_theory_of_the_Lorentz_group"]]'
    return repr_open_search


@fixture
def repr_json_return():
    return {
        "links": [
            "https://en.wikipedia.org/wiki/Representational_state_transfer",
            "https://en.wikipedia.org/wiki/Reproduction",
            "https://en.wikipedia.org/wiki/Reproductive_rights",
            "https://en.wikipedia.org/wiki/Reproductive_system",
            "https://en.wikipedia.org/wiki/Reproductive_isolation",
            "https://en.wikipedia.org/wiki/Representation_theory",
            "https://en.wikipedia.org/wiki/Representative_matches_in_Australian_rules_football",
            "https://en.wikipedia.org/wiki/Repressed_memory",
            "https://en.wikipedia.org/wiki/Reproductive_justice",
            "https://en.wikipedia.org/wiki/Representation_theory_of_the_Lorentz_group",
        ]
    }
