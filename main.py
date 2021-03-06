import random
import sys
import time

from lib import api, extract, stat, subset

s = subset.Subset()
w = api.WikiAPI()
e = extract.Extract()
st = stat.Stats()


# Create subset by cutoff -> python3 main.py cut 0.85
if len(sys.argv) == 3 and sys.argv[1] == 'cut':
    cutoff = sys.argv[2]
    d = s.file_to_dict()
    print('{} distinct names found'.format(len(d)))
    d = s.sort_dict(d)
    print('Total population is {}'.format(s.get_total_names(d)))
    d = s.cutoff_dict(d, cutoff)
    print('{} distinct names in subset'.format(len(d)))
    print('Total population in subset is {}'.format(s.get_total_names(d)))
    s.store_output(d, cutoff)

# Get urls -> python3 main.py urls 0.85
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
            time.sleep(random.randint(10, 35))

# Process countries -> python3 main.py countries
if sys.argv[1] == 'countries':
    urls = w.open_remaining_urls()

    d = e.open_frequencies()
    for k, v in urls.items():
        print('Processing {}'.format(k))

        urls = e.clean_urls(v, k)
        countries = e.urls_to_countries(urls)
        freq = e.countries_to_frequency(countries)

        print('Storing {} {}'.format(k, freq))
        e.save_record(d, k, freq)
        if len(freq) > 0:
            time.sleep(random.randint(20, 55))

# Show data -> python3 main.py show
if sys.argv[1] == 'show':
    d = e.open_frequencies()
    for k, v in d.items():
        print(' '.join([k, str(v)]))

# Process stats -> python3 main.py stats
if sys.argv[1] == 'stats':
    st.create_file()

# Aggregate data
if sys.argv[1] == 'agg':
    d = dict()
    total = 0
    with open('data/nat2018_labeled.csv', 'r') as f:
        next(f)
        for line in f.readlines():
            data = line.split(';')
            key = '\t'.join([data[4].replace('\n', ''), data[2]])
            if data[2] != 'XXXX':
                if key in d:
                    d[key] += int(data[3])
                else:
                    d[key] = int(data[3])
                total += int(data[3])
    print('Total population aggregated {}'.format(total))

    with open('data/nat2018_agg.csv', 'w') as f:
        for k, v in d.items():
            f.write('\t'.join([k, str(v)]) + '\n')
