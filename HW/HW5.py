import time

start_time = time.time()

def load_data():
    file_name = "dijkstraData.txt"
    #file_name = "HW5_Test1.txt"
    lines = [line.strip('\r\n') for line in open(file_name)]
    dic = {}
    for line in lines:
        if line.strip('\r\n') == '':
            continue
        temp = line.split(' ')
        if len(temp) == 1:
            temp = line.split('\t')
        temp = [a for a in temp if a != '']
        dic_row = {}
        for a_tuple in temp[1:]:
            #if a == '':
            #break
            (a,b) = a_tuple.split(',')
            a = int(a)
            b = int(b)
            dic_row[a] = b
        #print temp
        key = temp[0]
        dic[int(key)] = dic_row
    return dic

no_path = 1000000

def master():
    dic = load_data()
    A = naive(dic)
    print 'res', A[7],A[37],A[59],A[82],A[99],A[115],A[133],A[165],A[188],A[197]
    
def naive(dic):
    global no_path
    global X
    global A
    
    n = len(dic)
    
    X = [1]
    A = {}
    A[1] = 0
    B = {}
    B[1] = [0]
    
    while True:
        lvw = -1
        new_vertex = -1
        start_vertex = -1
        for v in X:
            connect_v = dic[v]
            for k1, v1 in connect_v.items():
                if k1 not in X:
                    #print 53, v, k1, v1, A
                    temp_l = A[v] + v1
                    if lvw == -1 or temp_l < lvw:
                        lvw = temp_l
                        new_vertex = k1
                        start_vertex = v
        A[new_vertex] = lvw
        X.append(new_vertex)
        #print 60, B, start_vertex, new_vertex
        B[new_vertex] = B[start_vertex] + [new_vertex]
        if len(X) == n:
            break
    #print 59, X, A
    #print 60, B
    return A
    
'''    
dic = load_data()
print dic
'''

master()

print time.time() - start_time
