import operator

import pytest

from lib import api, extract, subset


class TestIntegrity():

    def setup(self):
        s = subset.Subset()
        w = api.WikiAPI()
        e = extract.Extract()
        self.names = s.open_names('0.85')
        self.urls = w.open_urls()
        self.frequencies = e.open_frequencies()

    def test_names_count(self):
        assert len(self.names) == 780

    def test_names_get(self):
        assert self.names.get('1;JEAN') == 1916584

    def test_urls_count(self):
        assert len(self.urls) != 780

    @pytest.mark.skip(reason="tested")
    def test_urls_keys(self):
        assert self.urls.keys() == []

    @pytest.mark.skip(reason="tested")
    def test_urls_get_jean(self):
        assert self.urls.get('JEAN') == []

    @pytest.mark.skip(reason="tested")
    def test_urls_get_maelys(self):
        assert self.urls.get('MAËLYS') == []

    @pytest.mark.skip(reason="tested")
    def test_urls_get_cedric(self):
        assert self.urls.get('CÉDRIC') == []

    @pytest.mark.skip(reason="tested")
    def test_urls_get_jeremy(self):
        assert self.urls.get('JÉRÉMY') == []

    def test_diff_urls_names(self):
        _names = self.names.keys()
        _names = set([x.split(';')[1] for x in _names])
        _urls = set(self.urls.keys())
        assert _names.difference(_urls) == set()

    def test_count_total_urls(self):
        cnt = map(len, self.urls.values())
        assert sum(cnt) == 88729

    def test_count_total_names(self):
        assert sum(self.names.values()) == 72125408

    # @pytest.mark.skip(reason="must return 0")
    def test_has_no_freq(self):
        d = self.frequencies
        no_data = dict()
        for k, v in d.items():
            if len(v) == 0:
                no_data[k] = v
        assert no_data == 0
        # https://en.wikipedia.org/w/api.php?action=opensearch&search=TIMEO&limit=100&namespace=0&format=jsonfm

    def test_name_is_foreign(self):
        d = self.frequencies
        data = dict()
        for k, v in d.items():
            try:
                country = max(v.items(), key=operator.itemgetter(1))[0]
                if country != 'FR':
                    data[k] = country
            except Exception:
                continue
        assert len(data) > 1

    def test_distinct_stored_countries(self):
        d = self.frequencies
        countries = set()
        for _, v in d.items():
            for k, w in v.items():
                countries.add(k)
        assert len(countries) == 169

    def test_distinct_stored_countries_popularity(self):
        d = self.frequencies
        countries = dict()
        for _, v in d.items():
            for k, w in v.items():
                if k not in countries:
                    countries[k] = 1
                else:
                    countries[k] += 1
        assert len(countries) == 169
