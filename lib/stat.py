import operator

from lib import extract


class Stats():

    def __init__(self):

        self.CLUSTERS = {
          'ANGLO': ['GB', 'AU', 'ZA', 'CA', 'NZ', 'IE', 'US', 'SA'],
          'LATIN-EUROPE': ['IL', 'IT', 'PT', 'ES', 'FR', 'CH', 'BE', 'RO'],
          'NORDIC-EUROPE': ['FI', 'SE', 'DK', 'NO'],
          'GERMANIC-EUROPE': ['AT', 'NL', 'DE'],
          'EASTERN-EUROPE': ['HU', 'RU', 'KZ', 'AL', 'PL', 'GR', 'SI',
                             'GE', 'CZ', 'UA', 'BG', 'HR', 'RS', 'BY', 'SK', 'EE'],
          'LATIN-AMERICA': ['CR', 'VE', 'EC', 'MX', 'SV',
                            'CO', 'GT', 'BO', 'BR', 'AR', 'CL', 'CU', 'UY', 'PE'],
          'SUB-SAHARA AFRICA': ['NA', 'ZM', 'ZW', 'ZA', 'NG', 'CM',
                                'CI', 'SN', 'CD', 'KE'],
          'ARAB': ['QA', 'MA', 'TR', 'EG', 'KW', 'TN', 'DZ', 'LB', 'ML', 'SY',
                   'BF', 'IQ', 'PK', 'GN'],
          'SOUTHERN-ASIA': ['IN', 'ID', 'PH', 'MY', 'TH', 'IR'],
          'CONFUCIAN-ASIA': ['TW', 'SG', 'HK', 'KR', 'CN', 'JP', 'VN'],
        }
        self.filename = '/usr/src/app/data/nat2018.csv'
        self.outputfile = '/usr/src/app/data/nat2018_labeled.csv'
        self.frequencies = extract.Extract().open_frequencies()

    def get_cluster(self, country):
        for k, v in self.CLUSTERS.items():
            if country in v:
                return k
        return None

    def countries_to_cluster(self, countries):
        d = dict()
        for country, cnt in countries.items():
            cluster = self.get_cluster(country)
            if cluster in d:
                d[cluster] += cnt
            else:
                d[cluster] = cnt
        return d

    def dominant_cluster(self, clusters):
        try:
            dominant =  max(clusters.items(), key=operator.itemgetter(1))[0]
        except Exception:
            dominant = 'UNKNOWN'
        if dominant is None:
            dominant = 'UNKNOWN'
        return dominant

    def create_row(self, row):
        row = row.replace('\n', '')
        items = row.split(';')

        countries = self.frequencies.get(items[1], {})
        clusters = self.countries_to_cluster(countries)
        dominant = self.dominant_cluster(clusters)

        return ';'.join([row, dominant])

    def create_file(self):
        i = 0
        rows = []
        with open(self.filename) as f:
            for line in f:
                if i == 0:
                    header = ';'.join([line.replace('\n', ''), 'cluster'])
                    rows.append(header + '\n')
                else:
                    rows.append(self.create_row(line) + '\n')
                i += 1
        f.close()

        with open(self.outputfile, 'w') as f:
            for row in rows:
                f.write(row)
        f.close()
