#! python2
# coding: utf-8
import networkx


def get_edge_for_snap(filename):
    edges = []
    with open(filename, 'r') as f_open:
        for each_line in f_open:
            if each_line[0] != '#':
                s = each_line[:-1].split('\t')
                i = int(s[0])
                j = int(s[1])
                edges.append((i, j))
        return edges


if __name__ == '__main__':
    filename1 = 'H:/social_network_analysis/Email-Enron.txt'
    filename2 = 'H:/social_network_analysis/com-amazon.ungraph.txt'
    ed = get_edge_for_snap(filename2)

    # 21:03
    test_g = networkx.Graph(ed)
    networkx.average_shortest_path_length(test_g)
