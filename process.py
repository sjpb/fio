#!/usr/bin/env python3

NO_DATA = ''

import sys, json, csv, traceback

writer = csv.writer(sys.stdout, delimiter=',')
header = ['file', 'directory', 'name', 'mode', 'blocksize'] + ['bw_min', 'bw_mean', 'bw_max'] + ['iops_min', 'iops_mean', 'iops_max']
writer.writerow(header)
for arg in sys.argv[1:]:
    with open(arg) as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            writer.writerow([arg] + [NO_DATA] * (4 + 3 + 3))
            continue
        try:
            directory = data['global options']['directory']
            job1 = data['jobs'][0]
            blocksize = data['global options'].get('bs') or job1['job options']['bs']
            name = job1['job options']['name']
            mode = job1['job options']['rw']
            bw = [job1[mode][s] for s in ('bw_min', 'bw_mean', 'bw_max')]
            iops = [job1[mode][s] for s in ('iops_min', 'iops_mean', 'iops_max')]
            writer.writerow([arg, directory, name, mode, blocksize] + bw + iops)
        except KeyError as err:
            traceback.print_tb(err.__traceback__)
            writer.writerow([arg] + [NO_DATA] * (4 + 3 + 3))
            

        