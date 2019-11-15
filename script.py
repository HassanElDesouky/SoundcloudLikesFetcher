import csv

output = open("output.csv", "w", newline='')

writer = csv.writer(output)

with open("soundcloud.txt", "r") as f:
    for i, line in enumerate(f):
        link = ''
        name = ''
        if 'audibleTile__audibleHeading sc-truncate sc-font-light" href="' in line:
            find_link = line.find('audibleTile__audibleHeading sc-truncate sc-font-light" href="')
            if find_link != -1:
                find_link += len('audibleTile__audibleHeading sc-truncate sc-font-light" href="')
                find_end = line.find('"')
                link = line[find_link:-3]
                output.write(link + ',')
        if 'playableTile__mainHeadingLike' in line:
            arr = f.readlines(1)
            name = arr[1]
            output.write(name)
        link = ''
        name = ''

output.close()
