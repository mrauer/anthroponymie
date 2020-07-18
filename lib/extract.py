from urllib.parse import urlparse

import requests

import lxml.html


class Extract():

    def __init__(self):
        self.COUNTRIES = {'/wiki/Q38': 'IT',
                          '/wiki/Q159': 'RU',
                          '/wiki/Q145': 'GB',
                          '/wiki/Q869': 'TH',
                          '/wiki/Q142': 'FR'}

    def get_html(self, url):
        """Get HTML from an url."""
        r = requests.get(url)
        return r.content

    def parse_urls(self, html):
        """Parse urls from content."""
        doc = lxml.html.fromstring(html)
        return doc.xpath('//a/@href')

    def get_wikidata_ID(self, urls):
        """Get the structured wikidata ID."""
        ret = ''
        for url in urls:
            try:
                if url.find('https://www.wikidata.org') != -1:
                    ret = urlparse(url).path.split('/')[2]
                    return ret
            except Exception:
                continue
        return ret

    def get_country_from_wikidata(self, ID):
        """Find country code from Wikidata."""
        ret = None
        try:

            url = '/'.join(['https://www.wikidata.org/wiki', ID])
            html = self.get_html(url)
            urls = self.parse_urls(html)

            for url in urls:
                if url in self.COUNTRIES:
                    return self.COUNTRIES[url]
        except Exception:
            return ret
        return ret

    def get_countries(self, urls):
        """Get countries from list of urls."""
        pass

    def format_output(self, countries):
        """Format output for storage."""
        pass

    def save_record(self):
        """Save output into pickled dict."""
        pass
