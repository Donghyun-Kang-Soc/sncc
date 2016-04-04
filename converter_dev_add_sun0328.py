# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 15:54:51 2016

@author: user
"""
# 아래에 추가된 부분을 표시해놓았음.

class Sncc_converter:
    @staticmethod
    def self_loop_deleter(input_f, output_f, sep = "\t"):
    
        f = open(input_f, 'r')
        f_lines = f.readlines()
        edges_location = f_lines.index("*Edges\n")
        out_put = open("output_f", 'w')
        

        for line in f_lines[1:edges_location]:
            splited = line.split(sep)
            node_dict[str(splited[0])] = splited[1].rstrip('\n')
           
       
        edges_lines = f_lines[edges_location+1:]
        
        edge_sep = ''
        if '\t' in edges_lines[0]:
            edge_sep = "\t"
        elif ' ' in edges_lines[0]:
            edge_sep = ' ' 
        
        for line in edges_lines :
            splited_2 = line.split(edge_sep)
            
            
            if str(splited_2[0]) != str(splited_2[1]).rstrip('\n'):
                source = str(splited_2[0])
                target = str(splited_2[1]).rstrip('\n')
                edge_list = [node_dict.get(source) , node_dict.get(target)]
                out_put.write(edge_list[0] + "\t" + edge_list[1] + "\n")
        
        
        print("Done")
        f.close()
        out_put.close()
    
if __name__ == "__main__":
    Sncc_converter.self_loop_deleter('vignett37_network.net', 'test_37.txt')
    Sncc_converter.self_loop_deleter()
