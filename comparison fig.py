import csv

diff_dict = {}
# import csv
with open("data/comparison.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if row[5] and row[6]:
            if diff_dict.get(eval(row)):
                diff_dict[eval(row[6])] += [eval(row[5])]
            diff_dict[eval(row[6])] = eval(row[5])

            # dist.append(eval(row[5]))
            # count.append(eval(row[6]))

        # data.append(eval(row))

print(dist)
print(count)
