# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:24:24 2016

@author: user
"""


class Sncc_converter:
    @staticmethod
    
"""
nmf 파일을 txt 파일로 변환하면 node set 파일과 link set 파일 2개가 만들어짐.
Part 1은, node set 파일을 사용하여 "*vertice n" 파트를 기록하도록 함.
Part 2는, link set 파일을 사용하여 "*Edges" 파트를 Part 1의 out_put 파일에 추가하도록 함.
"""


"""
Part 1
"""

    import re
    
    f = open("C:\\Users\\user\\Documents\\Spyder\\vignett37_network_2_N_Main Nodeset.txt", 'r')
    f_lines = f.readlines()
    out_put = open("output_f", 'w')

    num_of_node = f_lines.count("\n")
    out_put = out_put.write("*Vertices" + " " + str(num_of_node) + "\n")
    
   
    sep = "\t"

    
    for line in f_lines[1:]:
        splited = line.split(sep)
        striped = [str(splited[0].strip('\"')), splited[1].strip('\"').rstrip('\"\"\n')]
        out_put = open("output_f", 'a')
        out_put = out_put.write(striped[0] + "\t" + '\"' + striped[1] + '\"' + "\n")
    
    f.close()
    out_put.close()
   
   
# out_put 파일에서 Vertices 개수 출력이 안됨. (num_of_node = f_lines.count("\n")으로 했을 때, 0으로 출력)   
# num_of_node_2 = f_lines.index('[\n+]') : 이렇게 해도 안됨
# num_of_node_3 = f_lines.index('^$') : 이렇게 해도 안됨
   
   
"""
Part 2
"""
    
    
    f = open("C:\\Users\\user\\Documents\\Spyder\\vignett37_network_2_L_vignett37_network_2.txt", 'r')
    f_lines = f.readlines()
    out_put = open("output_f", 'a')
    out_put = out_put.write("*Edges" + "\n")

    sep = "\t"

    for line in f_lines[1:]:
        
        splited = line.split(sep)
        source = splited[0].strip('\"')
        
        targets_num = 0
        
        for targets in splited[1:-1]:
            targets_num += 1
            targets_f = str(targets_num)
            times = targets[0]
            int_times = int(times)

            out_put = open("output_f", 'a')
            out_put = out_put.write(int_times*(str(source) + '\t' + targets_f + '\n'))
    
    print('Done')

    f.close()

# 이건 왜 안되는걸까: times = int(targets.rstrip('\.').rstrip('\n'))