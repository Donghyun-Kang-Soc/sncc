def function_name (input, output, directed = 'False', sep = 't'):
    i = open(input, 'r')
    lines = i.readlines()
    o = open(output, 'w')
    o.write('Source\tTarget\tType\tWeight\n')
    for line in lines:
        splited = line.split('\t')
        splited.append(splited[2])
        if directed == 'False':
            splited[2] = 'Undirected'
        else :
            splited[2] = 'Directed'
        splited[3] = splited[3].strip('\n')
        for k in range(0, 4):
            o.write(splited[k])
            o.write('\t')
        o.write('\n')
    i.close()
    o.close()
function_name ('input_sample - 복사본.txt', 'output_sample_haha.txt', directed = 'False', sep = 't')
