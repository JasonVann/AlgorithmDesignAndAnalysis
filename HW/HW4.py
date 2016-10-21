# HW4, find SCCs

def load_data():
    #file_name = "SCC.txt"
    file_name = "HW4_Test1.txt"
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

def master():
    dic = load_data()
    # Iter 1
    print 6, dic
    DFS_Loop(dic)
    print 7, dic
    
    # Iter 2
    

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
    for j in dic[i]:
        if j not in d_visited:
            DFS(dic, j)
    t += 1
    d_visited[i] = (s, t)
    print 37, d_visited
    print 38, dic


dic = load_data()
#print dic
#master()

t = 0
s = 9
d_visited = {}
DFS(dic, 9)
