import os
import pickle

import requests


class WikiAPI():

    def __init__(self):
        limit = 500
        self.root = ('https://fr.wikipedia.org/w/'
                     'api.php?action=opensearch&search=')
        self.params = ''.join(['&limit=', str(limit),
                               '&namespace=0&format=json'])

    def call_api(self, query):
        """Make an API call."""
        r = requests.get(''.join([self.root, query, self.params]))
        return r.json()[3]

    def open_urls(self):
        """Open a pickled file."""
        d = dict()
        output = '/usr/src/app/data/URLS.p'
        if os.path.exists(output):
            d = pickle.load(open(output, 'rb'))
        print('{} items in URLS.p'.format(len(d)))
        return d

    def open_remaining_urls(self):
        """Open the remaining urls to process."""
        d = dict()
        output = '/usr/src/app/data/URLS.p'
        frequency = '/usr/src/app/data/FREQUENCY.p'
        if os.path.exists(output):
            _d = pickle.load(open(output, 'rb'))
            if not os.path.exists(frequency):
                return _d
            f = pickle.load(open(frequency, 'rb'))
            for k, v in _d.items():
                if k not in f:
                    d[k] = v
        print('{} items to process in URLS.p'.format(len(d)))
        return d

    def check_if_record_exist(self, d, query):
        return True if query in d else False

    def save_record(self, d, query, data):
        """Store output in pickled dict."""
        if query not in d:
            d[query] = data
        output = ''.join(['/usr/src/app/data/URLS.p'])
        pickle.dump(d, open(output, 'wb'))
