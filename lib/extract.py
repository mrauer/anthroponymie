from urllib.parse import urlparse

import requests

import lxml.html


class Extract():

    def __init__(self):
        COUNTRIES = {'France': 'http://aaaa'}

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

    def get_countries(self, urls):
        """Get countries from list of urls."""
        pass

    def format_output(self, countries):
        """Format output for storage."""
        pass

    def save_record(self):
        """Save output into pickled dict."""
        pass


# get content
# convert to wikidata | https://www.wikidata.org/wiki/Q1756086
# convert to country code
