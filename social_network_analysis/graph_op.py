#! python2
# coding: utf-8
import copy


def t_shortest_path(t_am):
    t1 = get_weight_matrix(t_am)
    len_t = len(t1)
    k = 0
    while k < len_t:
        i = 0
        while i < len_t:
            j = 0
            while j < len_t:
                if t1[i][j] > t1[i][k] + t1[k][j]:
                    t1[i][j] = t1[i][k] + t1[k][j]
                j = j + 1
            i = i + 1
        k = k + 1
    return t1


def shortest_path_sparse(t_am, max_k):
    """用基于字典的稀疏矩阵来找到最小路径，有如下改进

    1.省去了自写的复制
    2.省去了标记没有路径
    3.占用空间小
    """
    t1 = copy.deepcopy(t_am)
    o = 0
    while o < max_k:
        for i, k in t1.iteritems():
            for j, m in k.iteritems():
                if o in t1[i] and o in t1:  # 先判断是否在字典中
                    if j in t1[o]:
                        if t1[i][j] > t1[i][o] + t1[o][j]:  # 再判断是否可取代
                            t1[i][j] = t1[i][o] + t1[o][j]
                            print(i, j, t1[i][j])
                            break
        o += 1
    return t1


def apl_sparse(tsp, nn):
    sums = 0
    for i in tsp.itervalues():  # 这种遍历方式就只看dict的值
        for j in i.itervalues():
            sums += j
    return 2 * sums / (nn * (nn - 1))*1.0


def average_path_length(t_am):
    tsp = t_shortest_path(t_am)
    sums = 0
    len_t = len(t_am)
    i = 0
    while i < len_t:
        j = 0
        while j < len_t:
            if tsp[i][j] != 999:
                sums = sums + tsp[i][j]
                # print(tsp[i][j])
            j = j + 1
            # print(tsp[i][j])
        i = i + 1
        # print(sums)
    if len_t < 2:
        apl = 0.0
    else:
        apl = 2 * sums / (len_t * (len_t - 1))
    return apl


def get_weight_matrix(t_am):
    t1 = copy.deepcopy(t_am)
    i = 0
    len_t = len(t1)
    while i < len_t:
        j = 0
        while j < len_t:
            if t1[i][j] == 0:
                t1[i][j] = 999
            j = j + 1
        # print(t_am[i])
        i = i + 1
    return t1


def create_zero_ad_matrix(num):
    z_t = []
    for i in range(num):
        tmp = []
        for j in range(num):
            tmp.append(0)
        z_t.append(tmp)
    return z_t
