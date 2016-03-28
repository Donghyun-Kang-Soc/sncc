def add_direct (input, output, directed = 'False', sep = '\t'):
    o = open(output, 'w')
    o.write('Source\tTarget\tType\tWeight\n')
    for line in open(input, 'r'):
        splited = line.split(sep)
        splited.append(splited[2])
        if directed == 'False':
            splited[2] = 'Undirected'
        else :
            splited[2] = 'Directed'
        splited[3] = splited[3].strip('\n')
        for k in range(0, 4):
            o.write(splited[k])
            o.write(sep)
        o.write('\n')
    o.close()
# add_direct ('input_sample.txt', 'output_sample.txt', directed = 'False', sep = '\t')
