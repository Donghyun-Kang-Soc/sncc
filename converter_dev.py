import add_direct

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
	
if __name__ == "__main__":
    Sncc_converter.net_to_edgelist('vignett130_network_1.net', 'test_130.txt')
    Sncc_converter.edgelist_to_net()
