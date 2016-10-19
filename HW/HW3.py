import random
import math

def rand_two2(left_vertices,arr):

    while True:
        u = random.randint(1, len(left_vertices) - 1)
        v = random.randint(1, len(left_vertices) - 1)
        if u != v:
            #Then make sure u and v are connected directly
            res = [k for k in arr if u in k and v in k]
            
            if len(res) > 0:
                break
    return (u, v)

def rand_two(dic, dic_visited):
    left_vertices = dic.keys()
    #u = random.randint(1, len(left_vertices) - 1)
    
    found = False
    while True:
        u = random.choice(left_vertices)
        #v = random.randint(1, len(left_vertices) - 1)
        v = random.choice(left_vertices)
        #print 27, dic, u, v
        if u != v and u not in dic_visited and v not in dic_visited:
            #Then make sure u and v are connected directly
            if v in dic[u]:
                break
            
    return (u, v)

def rand_contract(dic):
    visited = []
    #for i in range(len(all)):
    #left_vertices = [k[0] for k in arr]

    dic_visited = {}
    while True:
        (u, v) = rand_two(dic, dic_visited)
        #Assume v is absorbed by u
        print 41, dic, u, v
        val_u = dic[u]
        val_v = dic[v]
        #dic_visited[u] = val_u
        dic_visited[v] = val_v
        # remove edge u-v
        val_u.remove(v)
        val_v.remove(u)
        dic[u] = val_u
        dic[v] = val_v
        '''
        dic[u] = list(set(val_u+val_v))
        if u in dic[u]:
            dic[u].remove(u)
        #dic.pop(u)
        dic.pop(v)
        for key, val in dic.items():
            if v in val:
                val.remove(v)
                if u not in val and key != u:
                    #print 56, val, u, v, dic
                    val.append(u)
                    #print 49, val
                #if key == u and v in val:
        
                dic[key] = val
        '''
        print 59, dic, dic_visited, u, v
        if len(dic) - len(dic_visited) == 2:
            break
    #print dic, dic_visited
    return dic
    
def master():
    #Call multiple times
    
    dic = load_data()
    n = len(dic)
    cur = -1
    print 68, dic
    #for i in range(int(n**2*math.log(n))):
    for i in range(2):    
        dic2 = dict(dic)
        temp = rand_contract(dic2)
        #for key, val in temp.items():
        #count = len(val)
        count = len(dic2)
        if cur == -1 or count < cur:
            cur = count
            
    print 67, dic, dic2, cur
    
def load_data():
    file_name = "HW3_Test12.txt"
    lines = [line.strip("\r\n") for line in open(file_name)]
    
    dic = {}
    for line in lines:
        if len(line) > 0:
            a = line[1:].strip().split(' ')
            a = [int(b) for b in a]
            dic[int(line[0])] = a
    #print dic
    return dic

#dic = load_data()
#print rand_two(dic)
master()
