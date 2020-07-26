from lib import extract, stats


class TestStats():

    def setup(self):
        e = extract.Extract()
        s = stats.Stats()
        self.frequencies = e.open_frequencies()
        self.CLUSTERS = s.CLUSTERS
        self.POPULAR_LIMIT = 75

    def test_popular_countries(self):
        _d = dict()
        for k, v in self.frequencies.items():
            for country, cnt in v.items():
                if country in _d:
                    _d[country] += cnt
                else:
                    _d[country] = cnt

        d = dict((k, v) for k, v in _d.items() if v >= self.POPULAR_LIMIT)
        assert len(_d) == 169
        assert len(d) == 29

    def test_popular_countries_not_in_clusters(self):
        # Popular countries
        d = dict()
        for k, v in self.frequencies.items():
            for country, cnt in v.items():
                if country in d:
                    d[country] += cnt
                else:
                    d[country] = cnt
        d = dict((k, v) for k, v in d.items() if v >= self.POPULAR_LIMIT)
        all_countries = set(d.keys())

        # Countries in clusters
        countries = set()
        for v in self.CLUSTERS.values():
            for c in v:
                countries.add(c)

        assert len(all_countries.difference(countries)) == 0
        # assert all_countries.difference(countries) == 1
