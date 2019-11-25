import csv
import os

# Change base_path to yours
base_path = '/content/2011_09_26_drive_0056_sync'

paths = [
        '%s/%s' % (base_path, 'image_02'),
        '%s/%s' % (base_path, 'image_03'),
        ]

files = {}
for path in paths:
    for r, d, f in os.walk(path):
        for fname in f:
            if '.png' in fname:
                full_path = os.path.join(r, fname)
                pair = files.get(fname,[]);
                pair.append(full_path);
                if len(pair) == 2:
                    pair.append(full_path + ".pfm");
                files[fname] = pair


with open('sample.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(sorted(files.values()))
writeFile.close()
