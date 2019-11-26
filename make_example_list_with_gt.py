import csv
import os

# Change base_path to yours
base_path = "%s/%s" % (os.environ["HOME"], 'Downloads/2011_09_26')
image_path = '%s/%s' % (base_path, '2011_09_26_drive_0056_sync')

paths = [
        '%s/%s' % (image_path, 'image_02'),
        '%s/%s' % (image_path, 'image_03'),
        '%s/%s' % (image_path, 'image_03'),
        ]

files = {}
for path in paths:
    for r, d, f in os.walk(path):
        for fname in f:
            if '.png' in fname:
                full_path = os.path.join(r, fname)
                pair = files.get(fname,[]);
                pair.append(full_path);
                files[fname] = pair


with open('sample.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(sorted(files.values()))
writeFile.close()
