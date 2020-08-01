d = dict()
with open('../data/nat2018_labeled.csv', 'r') as f:
    next(f)
    for line in f.readlines():
        data = line.split(';')
        key = ';'.join([data[4].replace('\n', ''), data[2]])
        if data[2] != 'XXXX':
            if key in d:
                d[key] += int(data[3])
            else:
                d[key] = int(data[3])

with open('../data/nat2018_agg.csv', 'w') as f:
    for k, v in d.items():
        f.write(';'.join([k, str(v)]) + '\n')
