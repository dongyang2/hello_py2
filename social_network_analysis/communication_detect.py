#! python2
# coding: utf-8
import snap
import copy
from social_network_analysis import file_op


def out_ind_oud(g):
    """打印各点的id,出度，入度"""
    for i in g.Nodes():
        print "node id %d with out-degree %d and in-degree %d" % (
            i.GetId(), i.GetOutDeg(), i.GetInDeg())
    return


def out_modularity_cnm(g):
    """将cnm方法检测到的社区写入文件"""
    community_vector = snap.TCnComV()
    modularity = snap.CommunityCNM(g, community_vector)
    i = 0
    s = 'The modularity of the network is ' + str(modularity)
    com_set = []
    for community in community_vector:
        tmp_com = [i]
        # print "Community: "
        for j in community:
            # print(i)
            # print type(i)  # int
            tmp_com.append(j)
        com_set.append(tmp_com)
        i += 1
    file_op.write_file_li(com_set, 'H:/social_network_analysis/Email-Enron-result.txt', s)
    # print "The modularity of the network is %f" % modularity


def out_modularity_gn(g):
    """Girvan-Newman method"""
    community_vector = snap.TCnComV()
    modularity = snap.CommunityGirvanNewman(g, community_vector)
    for community in community_vector:
        print "Community: "
        for i in community:
            print i
    print "The modularity of the network is %f" % modularity


def degree_distribution(g):
    tmp = snap.TIntPrV()
    snap.GetDegCnt(g, tmp)
    for item in tmp:
        print "%d nodes with degree %d" % (item.GetVal2(), item.GetVal1())
    return


def diameter(g):
    """get diameter"""
    dia = snap.GetBfsFullDiam(g, 100)
    print('diameter, ', dia)
    return dia


def average_clustering_coefficient(g):
    """get the clustering coefficient of Graph"""
    ccf = snap.GetClustCf(g)
    print('average clustering coefficient, ', ccf)
    return ccf


def out_node_id(g):
    for i in g.Nodes():
        if i.GetId() > 1000000:
            print('a ha !')


def get_com_size(li):
    """li是二维数组"""
    len_li = []
    for i in li:
        len_li.append(len(i))
    return len_li


def get_size_top_n_com(li, n):
    len_l = len(li)
    if len_l < n:
        return False
    ll = get_com_size(li)
    i = 0
    while i < len_l:
        j = i + 1
        while j < len_l:
            if ll[j] >= ll[i]:
                tmp = ll[i]
                ll[i] = ll[j]
                ll[j] = tmp
                tp = li[i]
                li[i] = li[j]
                li[j] = tp
            j += 1
        i += 1
    top_n = []
    for i, j in enumerate(li):
        if i < n:
            top_n.append(j)
    return top_n


def get_snap_edge(g):
    """获得图g的边，存入字典"""
    ed = {}
    tmp = []
    ck = 0
    for i in g.Edges():
        # print(i1.GetSrcNId(), i1.GetDstNId())
        sn = i.GetSrcNId()
        if ck < sn:
            ed[ck] = tmp  # 数组存入字典
            ck = sn  # 重置字典下标
            tmp = []
        tn = i.GetDstNId()
        tmp.append(tn)
    return ed


def community_density(c, ae):
    """社区的密度，这个函数失败了，容易得到密度为0

    :param c: 社区里的所有点的ID
    :type  c: list
    :param ae: 图里所有点边
    :type  ae: dict
    """
    n = len(c)
    e = 0
    c.sort()  # ae里面存的是无向图的边，每个边只被存一次，所以这里c需要从小到大排
    # print(c)
    for i in range(n):
        j = i
        while j < n:
            if i in ae:
                if c[j] in ae[i]:
                    e += 1
            j += 1
    print(e)
    return 2 * e * 1.0 / (n * (n - 1)) * 1.0


def community_density_new(c, g):
    node_id = snap.TIntV()
    for i in c:
        node_id.Add(i)
    sub = snap.GetSubGraph(g, node_id)
    e = 0
    for i in sub.Edges():
        e += 1
    n = 0
    for i in sub.Nodes():
        n += 1
    # print('den', 2*e*1.0/(n*(n-1))*1.0)
    if n != 0 and n != 1:
        return 2*e*1.0/(n*(n-1))*1.0


def sort_com_by_size(li):
    len_l = len(li)
    tl = copy.deepcopy(li)
    ll = get_com_size(tl)
    i = 0
    while i < len_l:
        j = i + 1
        while j < len_l:
            if ll[j] >= ll[i]:
                tmp = ll[i]
                ll[i] = ll[j]
                ll[j] = tmp
                tp = tl[i]
                tl[i] = tl[j]
                tl[j] = tp
            j += 1
        i += 1
    return tl


if __name__ == '__main__':
    # print(snap.Version)
    filename1 = "H:/social_network_analysis/com-amazon.ungraph.txt"
    filename2 = 'H:/social_network_analysis/Email-Enron.txt'
    g6 = snap.LoadEdgeList(snap.PUNGraph, filename1, 0, 1)
    # out_node_id(g6)
    g5 = snap.LoadEdgeList(snap.PUNGraph, filename2, 0, 1)

    # diameter(g6)
    # degree_distribution(g6)
    # average_clustering_coefficient(g6)

    # 获得一个无向网络的所有边
    # edge5 = get_snap_edge(g5)
    # for j1, i1 in edge5.iteritems():
    #     if j1 < 10:
    #         print(j1, i1)  # 这里我惊奇地发现，snap读取无向图边的时候会按照无向图的保存，就是不分出边和入边

    # vector of pairs of integers (size, count)
    # CntV = snap.TIntPrV()
    # # get distribution of connected components (component size, count)
    # snap.GetWccSzCnt(G5, CntV)
    # # get degree distribution pairs (degree, count)
    # dd = snap.GetOutDegCnt(G5, CntV)
    # # # vector of floats
    # # EigV = snap.TFltV()
    # # # get first eigenvector of graph adjacency matrix
    # # snap.GetEigVec(G5, EigV)
    # # count the number of triads in G5,
    # triad = snap.GetTriads(G5)

    # print(snap.TCnComV())

    # 19:12开始跑，20：13没跑完，21：25没跑完，21：45报错了
    # [Program failed to allocate more memory. Solution-1: Get a bigger machine and a 64-bit compiler.]
    # 8:50 Enron开跑，8：52跑完
    # out_modularity_cnm(G5)
    # print(snap.GetModularity(G5, G5.Nodes()))

    li2 = file_op.read_file_li_new('H:/social_network_analysis/Email-Enron-result.txt', is_int=1)
    li3 = []
    for i2, i1 in enumerate(li2):
        # print(i1)
        if i2 != 0:
            li3.append(i1)
    # print(len(li3))
    top_max = 20
    t50 = get_size_top_n_com(li3, top_max)

    # w_name1 = 'H:/social_network_analysis/EE_top50.txt'
    # # file_op.write_file_li(t50, w_name1)

    import matplotlib.pyplot as plt

    # 把top n个社区的modularity画出来
    # community_mod = []
    # for i1 in t50:
    #     Nodes = snap.TIntV()
    #     for i2 in i1:
    #         Nodes.Add(i2)
    #     community_mod.append(snap.GetModularity(g5, Nodes))
    #     # print(snap.GetModularity(g5, Nodes), 'The size of this community is %d' % len(i1))
    fig = plt.figure()
    # plt.axis([0, 22, 0, 0.3])
    ax = range(top_max+1)[1:]
    # plt.ylim(0, 0.3)
    # plt.bar(ax, community_mod, color="green")
    # plt.xlabel("top %d community" % top_max)
    # plt.ylabel("modularity")
    # plt.title("top %d community modularity " % top_max)
    # plt.show()

    # 把top n个社区的密度画出来
    # edge1 = get_snap_edge(g5)
    # community_den = []
    # for i1 in t50:
    #     dens = community_density_new(i1, g5)
    #     community_den.append(dens)
    # for i1 in t50:
    #     den = community_density(i1, edge1)
    #     community_den.append(den)
    # print(community_den)
    # plt.bar(ax, community_den)
    # plt.xlabel("top %d community" % top_max)
    # plt.ylabel("density")
    # plt.title("top %d community density " % top_max)
    # plt.show()

    # 把所有社区密度画出来
    community_den = []
    li4 = sort_com_by_size(li3)
    for i1 in li4:
        dens = community_density_new(i1, g5)
        community_den.append(dens)
    # print(community_den)
    ax2 = range(len(community_den)+1)[1:]
    plt.xlabel('all the community (size big -> small)')
    plt.ylabel("density")
    plt.title('community density')
    plt.plot(ax2, community_den)
    plt.show()
