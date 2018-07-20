#read input
data = {}
with open('itcont.txt', mode='r') as file:
    file.readline()
    for line in file:
        ldata = line.strip().split(',')
        if ldata[3] in data.keys():
            data[ldata[3]][0] += float(ldata[4])
            data[ldata[3]][1][ldata[2]+' '+ldata[1]] = int(ldata[0])
        else:
            data[ldata[3]] = [float(ldata[4]), {ldata[2]+' '+ldata[1]:int(ldata[0])}]

# sort
data.update(sorted(data.items(), key=lambda t: t[1][0], reverse=True))

# write output
with open('top_cost_drug.txt', mode='w') as file:
    file.write('drug_name,num_prescriber,total_cost\n')
    for key,value in data.items():
        file.write(key+',{0:d},{1:d}\n'.format(len(value[1]), int(value[0])))
