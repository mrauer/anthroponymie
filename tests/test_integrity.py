import pytest

from lib import api, subset


class TestIntegrity():

    def setup(self):
        s = subset.Subset()
        w = api.WikiAPI()
        self.names = s.open_names('0.85')
        self.urls = w.open_urls()

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
