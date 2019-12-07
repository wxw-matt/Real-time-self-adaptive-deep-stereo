import csv
import os

# Change base_path to yours
# base_path = '/content/2011_09_26_drive_0056_sync'
base_path = "%s/%s" % (os.environ["HOME"], 'Downloads/2011_09_26')
image_path = '%s/%s' % (base_path, '2011_09_26_drive_0056_sync')

paths = [
        '%s/%s' % (image_path, 'image_00'),
        '%s/%s' % (image_path, 'image_01'),
        ]

files = {}
current_path = os.path.dirname(os.path.realpath(__file__))
f = open("null.png", "w+")

for i in range(0,253894):
    f.write("\0")
f.close()

for path in paths:
    for r, d, f in os.walk(path):
        for fname in f:
            if '.png' in fname:
                full_path = os.path.join(r, fname)
                pair = files.get(fname,[]);
                pair.append(full_path);
                if len(pair) == 2:
                    pair.append(current_path + "/null.png")
                files[fname] = pair


with open('sample.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(sorted(files.values()))
writeFile.close()
