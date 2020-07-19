import random
import sys
import time

from lib import api, subset

s = subset.Subset()
w = api.WikiAPI()

# get urls
if len(sys.argv) == 3 and sys.argv[1] == 'urls':
    cutoff = sys.argv[2]
    names = s.open_names(cutoff)
    urls = w.open_urls()
    for k, v in names.items():
        gender, query = k.split(';')
        if not w.check_if_record_exist(urls, query):
            print('Processing {}'.format(query))
            data = w.call_api(query)
            w.save_record(urls, query, data)
            time.sleep(random.randint(20, 55))

# extract countries
if sys.argv[1] == 'countries':
    print('in c')

# print(sys.argv)

# urls = w.open_urls()
# for k, v in urls.items():
#    print(k +' '+ str(len(v)))
