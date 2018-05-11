#! python2
# coding: utf-8
from social_network_analysis import graph_op
import copy


def write_file_li(li, filename, title=''):
    """写一个数组到文件中

    :param li       要写入的数组
    :type li        list
    :param filename 写入的文件名
    :type filename  str
    :param title    标题，会写入文件第一行
    :type title     str
    """
    f = open(filename, 'w')
    if title != '':
        f.write(title + '\n')
    if type(li[0]) is not list:
        for i in li:
            f.write(str(i) + ' ')
        f.write('\n')
    else:
        for i in li:
            for j in i:
                f.write(str(j) + ' ')
            f.write('\n')
    f.close()


def write_zero_adjacency_matrix(num, filename):
    f = open(filename, 'w')
    for i in range(num):
        for j in range(num):
            f.write('0 ')
        f.write('\n')
    return


def read_file_li(filename, title=0, is_int=0):
    """读取文件内容，每一行存入一个数组，返回一个二维数组"""
    if title != 0 and title != 1:
        return False
    with open(filename, 'r') as f_open:
        file_content = []
        for k, each_line in enumerate(f_open):
            if k == 0 and title == 1:
                # print(each_line)
                file_content.append(each_line[:-1])
            else:
                word = []
                for i in each_line.split(' ')[:-1]:
                    if is_int == 1:
                        word.append(int(i))
                    else:
                        word.append(i)
                file_content.append(word)
        return file_content


def read_file_li_new(filename, title=0, is_int=0):
    """读取文件内容，每一行存入一个数组，返回一个二维数组"""
    if title != 0 and title != 1:
        return False
    with open(filename, 'r') as f_open:
        file_content = []
        for k, each_line in enumerate(f_open):
            if k == 0 and title == 1:
                # print(each_line)
                file_content.append(each_line[:-1])
            elif k != 0:
                word = []
                for i in each_line.split(' ')[1:-1]:
                    if is_int == 1:
                        word.append(int(i))
                    else:
                        word.append(i)
                file_content.append(word)
        return file_content


def get_adj_matrix_for_snap(matrix_fil, filename, out_file):
    # am = read_file_li(matrix_fil, is_int=1)
    am = {}
    with open(filename, 'r') as f_open:
        ca = -1
        max_k = 0
        tmp_k = 0
        # for k, each_line in enumerate(f_open):
        #     if k == 20:
        #         break
        for each_line in f_open:
            if each_line[0] != '#':
                tmp_k += 1
                s = each_line[:-1].split('\t')
                i = int(s[0])
                if ca != i:  # 关键代码 —— 这里必须要把tmp字典内容重置
                    tmp = {}
                    ca = i
                    if tmp_k >= max_k:
                        max_k = tmp_k
                        tmp_k = 0
                j = int(s[1])
                tmp[j] = 1
                # print(i, j, am)
                am[ca] = tmp
        # print(am)
        return am, max_k


def traverse_dict(dic):
    for i, k in dic.iteritems():
        # print(i,k)
        for j, m in k.iteritems():
            print(j, m)


if __name__ == '__main__':
    li1 = [[1, 2, 3], [2, 3, 4]]
    w_name1 = 'H:/social_network_analysis/result1.txt'
    filename1 = 'H:/social_network_analysis/Email-Enron.txt'
    filename2 = 'H:/social_network_analysis/com-amazon.ungraph.txt'
    w_name2 = 'H:/social_network_analysis/EE_adjacent_matrix.txt'  # 0矩阵
    w_name3 = 'H:/social_network_analysis/EE_a_m_new.txt'  # 邻接矩阵
    tl1 = 'aa'
    # write_file_li(li1, w_name1, tl1)
    # print(read_file_li(w_name1, 1))

    num_node = 36692
    num_node2 = 334863
    # write_zero_adjacency_matrix(num_node, w_name2)
    # 20:37~20:41 Email-Enron
    # Amazon 21:34~21:45
    tm, mk = get_adj_matrix_for_snap(w_name2, filename2, w_name3)
    print('adjacent matrix get. And mk = %d' % mk)
    mt = graph_op.shortest_path_sparse(tm, mk)
    print('shortest path matrix get.')
    # print(mt)
    print(graph_op.apl_sparse(mt, num_node2))
    # for i1, i2 in tm.iteritems():
    #     for j1,j2 m in i2.iteritems():
    #         if tm[i1][j1] ==1:
    #             tm[i1][j1] = 2

    # print(i2)
    # print(tm)


