from lib import api, extract


class TestExtract():

    def setup(self):
        w = api.WikiAPI()
        self.urls = w.open_urls()
        self.e = extract.Extract()
        self.fr_url = 'https://fr.wikipedia.org/wiki/Jean-Baptiste_Colbert'
        self.it_url = 'https://fr.wikipedia.org/wiki/Lorenzo_Insigne'

    def test_get_one_url(self):
        assert self.urls.get('JEAN')[0] == self.fr_url

    def test_get_another_url(self):
        assert self.urls.get('LORENZO')[0] == self.it_url

    def test_get_html_from_url(self):
        html = self.e.get_html(self.it_url)
        assert len(html) > 1

    def test_parse_urls(self):
        html = self.e.get_html(self.it_url)
        urls = self.e.parse_urls(html)
        assert len(urls) > 1

    def test_get_wikidata_ID(self):
        html = self.e.get_html(self.it_url)
        urls = self.e.parse_urls(html)
        assert self.e.get_wikidata_ID(urls) == 'Q1756086'

    def test_another_wikidata_ID(self):
        url = self.fr_url
        html = self.e.get_html(url)
        urls = self.e.parse_urls(html)
        assert self.e.get_wikidata_ID(urls) == 'Q188971'

    def test_get_country_from_wikidata(self):
        country = self.e.get_country_from_wikidata('Q1756086')
        assert country == 'IT'

    def test_get_country_from_wikidata_bis(self):
        country = self.e.get_country_from_wikidata('Q188971')
        assert country == 'FR'

    def test_get_country_from_wikidata_none(self):
        country = self.e.get_country_from_wikidata('Q46384')
        assert country is None
