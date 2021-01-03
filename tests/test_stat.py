from lib import extract, stat


class TestStats():

    def setup(self):
        e = extract.Extract()
        self.s = stat.Stats()
        self.frequencies = e.open_frequencies()
        self.CLUSTERS = self.s.CLUSTERS
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

    def test_popular_countries_not_in_clusters_cnt(self):
        # Popular countries
        d, ret = {}, {}
        for k, v in self.frequencies.items():
            for country, cnt in v.items():
                if country in d:
                    d[country] += cnt
                else:
                    d[country] = cnt
        d = dict((k, v) for k, v in d.items() if v >= self.POPULAR_LIMIT)

        clusters_countries = [j for i in self.CLUSTERS.values() for j in i]
        for k, v in d.items():
            if k not in clusters_countries:
                ret[k] = v
        assert ret == 1

    def test_get_cluster(self):
        assert self.s.get_cluster('FR') == 'LATIN-EUROPE'
        assert self.s.get_cluster('MX') == 'LATIN-AMERICA'

    def test_countries_to_cluster(self):
        d = {'LB': 5, 'US': 1, 'TN': 12, 'SA': 1, 'DZ': 3,
             'FR': 2, 'LY': 1, 'MA': 2, 'EG': 2, 'PS': 1}
        assert self.s.countries_to_cluster(d) == {'ARAB': 24, 'ANGLO': 1,
                                                  None: 3, 'LATIN-EUROPE': 2}

    def test_dominant_cluster(self):
        d = {'ARAB': 24, 'ANGLO': 1, None: 3, 'LATIN-EUROPE': 2}
        assert self.s.dominant_cluster(d) == 'ARAB'

    def test_create_row(self):
        row = '1;GEORGES;1900;5659'
        assert self.s.create_row(row) == '1;GEORGES;1900;5659;LATIN-EUROPE'

        row = '1;BRANDON;1995;1328'
        assert self.s.create_row(row) == '1;BRANDON;1995;1328;UNKNOWN'

        row = '1;BRANDON;1995;1328'
        assert self.s.create_row(row) == '1;BRANDON;1995;1328;UNKNOWN'

        row = '1;KEVIN;1993;11241'
        assert self.s.create_row(row) == '1;KEVIN;1993;11241;ANGLO'
