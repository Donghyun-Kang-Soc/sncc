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
"""
add_direct ('input_sample.txt', 'output_sample.txt', directed = 'False', sep = '\t')

input_sample.txt

58767022	69625706	1
175440989	238901269	1
118720645	1256720508	1
2882782490	2471684046	1
319114948	264196770	1
.
.
.

output_sample.txt

Source	Target	Type	Weight
58767022	69625706	Directed	1
175440989	238901269	Directed	1
118720645	1256720508	Directed	1
2882782490	2471684046	Directed	1
319114948	264196770	Directed	1
.
.
.
"""
