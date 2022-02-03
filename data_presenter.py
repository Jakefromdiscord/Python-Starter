open_file = open('CupcakeInvoices.csv')

for line in open_file:
    line = line.strip('\n').split(',')
    print(line)

for line in open_file:
    line = line.strip('\n').split(',')
    print(line[2])

for line in open_file:
    line = line.strip('\n').split(',')
    print(float(line[4]) * int(line[3]))

total = 0

for line in open_file:
    
    line = line.split(',')
    total = total + (float(line[4]) * int(line[3]))

print(round(total,2))

open_file.close()