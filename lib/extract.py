from urllib.parse import urlparse

import requests

import lxml.html


class Extract():

    def __init__(self):
        self.iso_path = '/usr/src/app/data/.iso'

        self.COUNTRIES = {
          'Q228': 'AD',
          'Q55': 'NL',
          'Q889': 'AF',
          'Q781': 'AG',
          'Q25228': 'AI',
          'Q222': 'AL',
          'Q399': 'AM',
          'Q916': 'AO',
          'Q51': 'AQ',
          'Q414': 'AR',
          'Q16641': 'AS',
          'Q40': 'AT',
          'Q408': 'AU',
          'Q21203': 'AW',
          'Q5689': 'AX',
          'Q227': 'AZ',
          'Q225': 'BA',
          'Q244': 'BB',
          'Q902': 'BD',
          'Q31': 'BE',
          'Q965': 'BF',
          'Q219': 'BG',
          'Q398': 'BH',
          'Q1025': 'MR',
          'Q962': 'BJ',
          'Q25362': 'BL',
          'Q819': 'LA',
          'Q921': 'BN',
          'Q750': 'BO',
          'Q27561': 'BQ',
          'Q155': 'BR',
          'Q778': 'BS',
          'Q917': 'BT',
          'Q23408': 'BV',
          'Q963': 'BW',
          'Q184': 'BY',
          'Q242': 'BZ',
          'Q16': 'CA',
          'Q36004': 'CC',
          'Q974': 'CD',
          'Q929': 'CF',
          'Q971': 'CG',
          'Q39': 'CH',
          'Q1008': 'CI',
          'Q26988': 'CK',
          'Q298': 'CL',
          'Q1009': 'CM',
          'Q148': 'CN',
          'Q739': 'CO',
          'Q800': 'CR',
          'Q241': 'CU',
          'Q25279': 'CW',
          'Q31063': 'CX',
          'Q229': 'CY',
          'Q213': 'CZ',
          'Q977': 'DJ',
          'Q784': 'DM',
          'Q786': 'DO',
          'Q262': 'DZ',
          'Q736': 'EC',
          'Q191': 'EE',
          'Q79': 'EG',
          'Q6250': 'EH',
          'Q29': 'ES',
          'Q33': 'FI',
          'Q712': 'FJ',
          'Q702': 'FM',
          'Q4628': 'FO',
          'Q142': 'FR',
          'Q1000': 'GA',
          'Q145': 'GB',
          'Q769': 'GD',
          'Q230': 'GE',
          'Q3769': 'GF',
          'Q117': 'GH',
          'Q223': 'GL',
          'Q1005': 'GM',
          'Q1006': 'GN',
          'Q17012': 'GP',
          'Q983': 'GQ',
          'Q41': 'GR',
          'Q35086': 'GS',
          'Q774': 'GT',
          'Q16635': 'GU',
          'Q1007': 'GW',
          'Q734': 'GY',
          'Q8646': 'HK',
          'Q131198': 'HM',
          'Q783': 'HN',
          'Q224': 'HR',
          'Q790': 'HT',
          'Q28': 'HU',
          'Q252': 'ID',
          'Q27': 'IE',
          'Q801': 'IL',
          'Q9676': 'IM',
          'Q668': 'IN',
          'Q796': 'IQ',
          'Q794': 'IR',
          'Q189': 'IS',
          'Q38': 'IT',
          'Q785': 'JE',
          'Q766': 'JM',
          'Q810': 'JO',
          'Q17': 'JP',
          'Q114': 'KE',
          'Q813': 'KG',
          'Q424': 'KH',
          'Q710': 'KI',
          'Q970': 'KM',
          'Q763': 'KN',
          'Q423': 'KP',
          'Q884': 'KR',
          'Q817': 'KW',
          'Q5785': 'KY',
          'Q232': 'KZ',
          'Q822': 'LB',
          'Q760': 'LC',
          'Q347': 'LI',
          'Q854': 'LK',
          'Q1014': 'LR',
          'Q1013': 'LS',
          'Q37': 'LT',
          'Q32': 'LU',
          'Q211': 'LV',
          'Q1016': 'LY',
          'Q1028': 'MA',
          'Q235': 'MC',
          'Q217': 'MD',
          'Q236': 'ME',
          'Q126125': 'MF',
          'Q1019': 'MG',
          'Q709': 'MH',
          'Q221': 'MK',
          'Q912': 'ML',
          'Q836': 'MM',
          'Q711': 'MN',
          'Q14773': 'MO',
          'Q16644': 'MP',
          'Q17054': 'MQ',
          'Q13353': 'MS',
          'Q233': 'MT',
          'Q1027': 'MU',
          'Q826': 'MV',
          'Q1020': 'MW',
          'Q96': 'MX',
          'Q833': 'MY',
          'Q1029': 'MZ',
          'Q1030': 'NA',
          'Q33788': 'NC',
          'Q1032': 'NE',
          'Q31057': 'NF',
          'Q1033': 'NG',
          'Q811': 'NI',
          'Q20': 'NO',
          'Q837': 'NP',
          'Q697': 'NR',
          'Q34020': 'NU',
          'Q664': 'NZ',
          'Q842': 'OM',
          'Q804': 'PA',
          'Q419': 'PE',
          'Q30971': 'PF',
          'Q691': 'PG',
          'Q928': 'PH',
          'Q843': 'PK',
          'Q36': 'PL',
          'Q34617': 'PM',
          'Q35672': 'PN',
          'Q1183': 'PR',
          'Q219060': 'PS',
          'Q45': 'PT',
          'Q695': 'PW',
          'Q733': 'PY',
          'Q846': 'QA',
          'Q17070': 'RE',
          'Q218': 'RO',
          'Q403': 'RS',
          'Q159': 'RU',
          'Q1037': 'RW',
          'Q851': 'SA',
          'Q685': 'SB',
          'Q1042': 'SC',
          'Q1049': 'SD',
          'Q34': 'SE',
          'Q334': 'SG',
          'Q26778294': 'SH',
          'Q215': 'SI',
          'Q842829': 'SJ',
          'Q214': 'SK',
          'Q1044': 'SL',
          'Q238': 'SM',
          'Q1041': 'SN',
          'Q1045': 'SO',
          'Q730': 'SR',
          'Q958': 'SS',
          'Q1039': 'ST',
          'Q792': 'SV',
          'Q26273': 'SX',
          'Q858': 'SY',
          'Q1050': 'SZ',
          'Q18221': 'TC',
          'Q657': 'TD',
          'Q129003': 'TF',
          'Q945': 'TG',
          'Q869': 'TH',
          'Q863': 'TJ',
          'Q36823': 'TK',
          'Q574': 'TL',
          'Q874': 'TM',
          'Q948': 'TN',
          'Q678': 'TO',
          'Q43': 'TR',
          'Q754': 'TT',
          'Q672': 'TV',
          'Q865': 'TW',
          'Q924': 'TZ',
          'Q212': 'UA',
          'Q1036': 'UG',
          'Q16645': 'UM',
          'Q30': 'US',
          'Q77': 'UY',
          'Q265': 'UZ',
          'Q237': 'VA',
          'Q757': 'VC',
          'Q717': 'VE',
          'Q25305': 'VG',
          'Q11703': 'VI',
          'Q881': 'VN',
          'Q686': 'VU',
          'Q35555': 'WF',
          'Q683': 'WS',
          'Q805': 'YE',
          'Q17063': 'YT',
          'Q258': 'ZA',
          'Q953': 'ZM',
          'Q954': 'ZW'
        }

    def wiki_to_iso(self):
        """Populates the COUNTRIES var."""
        d = dict()
        value = None
        with open(self.iso_path) as f:
            for line in f.readlines():
                if line.find('/') != -1:
                    if line.find('ISO_3166-2') == -1:
                        key = line.replace('\n', '')

                    else:
                        value = line.replace(
                            '/wiki/ISO_3166-2:', '').replace('\n', '')
                if value:
                    d[key] = value
                    value = None
        return d

    def country_to_id(self, d):
        """Replace key of dict by country ID."""
        new_d = dict()
        for k, v in d.items():
            print(k)
            url = ''.join(['https://en.wikipedia.org', k])
            html = self.get_html(url)
            urls = self.parse_urls(html)
            ID = self.get_wikidata_ID(urls)
            new_d[ID] = v
        return new_d

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
                k = url.replace('/wiki/', '')
                if k in self.COUNTRIES:
                    return self.COUNTRIES[k]
        except Exception:
            return ret
        return ret

    def urls_to_countries(self, urls):
        """Convert a list of urls to the corresponding countries."""
        ret = []
        for url in urls:
            html = self.get_html(url)
            urls = self.parse_urls(html)
            ID = self.get_wikidata_ID(urls)
            country = self.get_country_from_wikidata(ID)
            ret.append(country)
            print(' '.join([url, country]))
        return ret

    def save_record(self):
        """Save output into pickled dict."""
        pass
