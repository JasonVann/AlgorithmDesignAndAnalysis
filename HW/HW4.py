# HW4, find SCCs

def load_data():
    #file_name = "SCC.txt"
    file_name = "HW4_Test3.txt"
    lines = [line.strip("\r\n") for line in open(file_name)]
    dic = {}
    for line in lines:
        if len(line) > 0:
            line = line.strip().split('\t')
            if len(line) == 1:
                line = line[0].strip().split(' ')
            key = int(line[0])
            val = int(line[1])

            #print key, val
            if key not in dic:
                dic[key] = [val]
            else:
                dic[key] = dic[key] + [val]

    #print dic
    return dic

def get_Grev(dic):
    dic_r = {}
    for key, val in dic.items():
        for v in val:
            if v in dic_r:
                dic_r[v] = dic_r[v] + [key]
            else:
                dic_r[v] = [key]
    print dic_r
    return dic_r

def master():
    global d_visited
    dic = load_data()
    dic_r = get_Grev(dic)
    
    # Iter 1
    print 6, dic_r
    DFS_Loop(dic_r)
    print 7, dic_r
    
    # Iter 2
    dic3 = {}
    dic_replace = {}
    for k, v in d_visited.items():
        (s, t) = v
        dic_replace[k] = t

    print 53, dic_replace
    print 55, 'Now iter2'
    dic_iter2 = {}
    #for i in range(1, len(dic) + 1):
    for k, v in dic.items():
        k2 = dic_replace[k]
        v2 = [dic_replace[e] for e in v]
        dic_iter2[k2] = v2
    print 61, dic_iter2
    #return
    #print 49, d_visited
    #print 50, dic
    #print 51, dic3
    #return
    DFS_Loop(dic_iter2)
    print 57, dic_iter2
    print 58, d_visited
    leaders = []
    d_res = {}
    for v in d_visited.values():
        (a, b) = v
        if a not in d_res:
            d_res[a] = [b]
            leaders += [a]
        else:
            d_res[a] += [b]
    
    print 77, leaders, d_res
    group = d_res.values()
    count = [len(e) for e in group]
    print count
    count += [0,0,0,0,0]
    count.sort(reverse=True)
    print count[:5]
    

def DFS_Loop(dic):
    global d_visited
    global t
    global s
    d_visited = {}
    t = 0
    s = -1
    n = len(dic)
    for i in range(n, 0, -1):
        if i not in d_visited:
            s = i
            DFS(dic, i)
    print 25, d_visited
    
def DFS(dic, i):
    global d_visited
    global t
    global s # leader
    d_visited[i] = s
    print 74, i, s, t, d_visited
    print 109, i, dic
    for j in dic[i]:
        if j not in d_visited:
            DFS(dic, j)
    t += 1
    d_visited[i] = (s, t)
    print 37, i, s, t, d_visited
    print 38, dic


dic = load_data()
print 75, dic
#dic_r = get_Grev(dic)
#print 77, dic_r
master()

'''
t = 0
s = 9
d_visited = {}
DFS(dic, 9)
'''
