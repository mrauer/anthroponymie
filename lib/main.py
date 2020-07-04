

firstnames = set()
with open('/usr/src/app/data/nat2018.csv') as f:
    next(f)
    for line in f:
        data = line.split(';')
        firstnames.add(data[1])

print(len(firstnames))