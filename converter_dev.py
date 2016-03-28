"""
1번 작업(1)
- node키(번호)와 값("단어")을 갖는 dictionary "node_dict" 생성.
- break문을 쓰는 대신, '\t'을 포함하는 경우만 돌도록 하여 *vertices부분 분리
"""

class Sncc_converter:
    @staticmethod
    def net_to_edgelist(input_f, output_f, sep = "\t"):
        node_dict = {}
        
        f = open(input_f, 'r')
        f_lines = f.readlines()
        edges_location = f_lines.index("*Edges\n")
        out_put = open(output_f, 'w')
    
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
            source = str(splited_2[0])
            target = str(splited_2[1]).rstrip('\n')
           
            edge_list = [node_dict.get(source) , node_dict.get(target)]
            out_put.write(edge_list[0] + "\t" + edge_list[1] + "\n")
        
        """
        3번 작업
        -"Done" 출력하고 작업 마무리
        """
        print("Done")
        f.close()
        out_put.close()
    """
    self_loop 제거기
    """
    
    def edgelist_self_erase(input_f, output_f, sep):
        pass
    @staticmethod
    def edgelist_to_net():
        print ('yes')
    
    def edge_to_gephi_edge(input_f, output_f, directed = False, sep = '\t')
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
                o.write('\t')
            o.write('\n')
        i.close()
        o.close()
	
if __name__ == "__main__":
    Sncc_converter.net_to_edgelist('vignett130_network_1.net', 'test_130.txt')
    Sncc_converter.edgelist_to_net()
