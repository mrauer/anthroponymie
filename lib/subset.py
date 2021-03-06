import os
import pickle


class Subset():

    def __init__(self):
        self.filename = '/usr/src/app/data/nat2018.csv'

    def file_to_dict(self):
        """Convert file data to dict."""
        d = dict()
        with open(self.filename) as f:
            next(f)  # skip first line
            for line in f:
                data = line.split(';')

                k = ';'.join([data[0], data[1]])
                v = int(data[3])

                if k in d:
                    d[k] += v
                else:
                    d[k] = v
        return d

    def sort_dict(self, d):
        """Order dict data in descending order."""
        return {k: v for k, v in sorted(d.items(),
                key=lambda item: item[1], reverse=True)}

    def show_n_results(self, d, n):
        """Show the n results from d."""
        i = 0
        for k, v in d.items():
            print(' '.join([k, str(v)]))
            i += 1
            if i == n:
                break

    def get_total_names(self, d):
        """Compute total names."""
        total = 0
        for k, v in d.items():
            total += v
        return total

    def cutoff_dict(self, d, cutoff):
        """Return a sub dict by cutoff."""
        total = self.get_total_names(d)
        target = (float(cutoff) * (
            total + d.get('1;_PRENOMS_RARES') + d.get('2;_PRENOMS_RARES')))
        limit = 0
        new_d = dict()
        for k, v in d.items():
            limit += v
            if limit >= target:
                break
            if k not in ['1;_PRENOMS_RARES', '2;_PRENOMS_RARES']:
                new_d[k] = v
        return new_d

    def store_output(self, d, cutoff):
        """Store output as pickled dict."""
        output = ''.join(['/usr/src/app/data/NAMES_', str(cutoff), '.p'])
        if not os.path.exists(output):
            pickle.dump(d, open(output, 'wb'))

    def open_names(self, cutoff):
        """Open a pickled file."""
        d = dict()
        output = ''.join(['/usr/src/app/data/NAMES_', str(cutoff), '.p'])
        if os.path.exists(output):
            d = pickle.load(open(output, 'rb'))
        print('{} items in NAMES_{}.p'.format(len(d), cutoff))
        return d
