# HW4, find SCCs
#import resource
import sys
#resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(3*10**8)

import time
start_time = time.time()

def gen_test():
    file_name = "SCC.txt"
    #file_name = "HW4_Test6.txt"
    to_name = "SCC_8.txt" 
    n = 8
    target = open(to_name, 'w')

    target.truncate()
    
    lines = [line.strip("\r\n") for line in open(file_name)]
    dic = {}
    for line in lines:
        if len(line) > 0:
            line = line.strip().split('\t')
            if len(line) == 1:
                line = line[0].strip().split(' ')
            key = int(line[0])
            val = int(line[1])

            if key > n or val > n:
                continue

            key = str(key)
            val = str(val)

            #print key, val

            target.write(key)
            target.write('\t')
            target.write(val)
            target.write('\n')
            
    #print dic
    return dic

#gen_test()

def load_data():
    file_name = "SCC.txt"
    #file_name = "HW4_Test4.txt"
    #file_name = "pa4_test_case_6.txt" #[261,244,219,198,196]
    file_name = "SCC_100K.txt"
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
    #print dic_r
    return dic_r

'''
10K: 0.13
50K: 38
100K: 250
'''

def master():
    global d_visited
    global n
    global start_time
    
    dic = load_data()
    dic_r = get_Grev(dic)
    #print 46, dic
    n = max(max(dic.keys()), max(dic_r.keys()))
    
    print(44, n, 'a', time.time() - start_time)
    
    # Iter 1
    #print 6, dic_r
    DFS_Loop(dic_r)
    #print 7, dic_r
    
    #print 56, dic_r
    #print 57, d_visited
    #return
    
    # Iter 2
    dic3 = {}
    dic_replace = {}
    for k, v in d_visited.items():
        (s, t) = v
        dic_replace[k] = t

    #print 53, dic_replace
    
    print(55, 'Now iter2')
    dic_iter2 = {}
    #for i in range(1, len(dic) + 1):
    for k, v in dic.items():
        k2 = dic_replace[k]
        v2 = [dic_replace[e] for e in v]
        dic_iter2[k2] = v2
    #print 61, dic_iter2
    #return
    #print 49, d_visited
    #print 79, dic_replace
    #print 50, dic
    #print 51, dic3
    #print 82, dic_iter2
    #return
    DFS_Loop(dic_iter2)
    #print 57, dic_iter2
    #print 58, d_visited
    leaders = []
    d_res = {}
    for v in d_visited.values():
        (a, b) = v
        if a not in d_res:
            d_res[a] = [b]
            leaders += [a]
        else:
            d_res[a] += [b]
    
    #print 77, leaders, d_res
    group = d_res.values()
    count = [len(e) for e in group]
    #print count
    count += [0,0,0,0,0]
    count.sort(reverse=True)
    print(count[:5])
    
def DFS_Loop(dic):
    global d_visited
    global t
    global s
    global n
    d_visited = {}
    t = 0
    s = -1
    #n = max(dic.keys())
    for i in range(n, 0, -1): 
        #print 98, i, dic
        if i not in dic and i not in d_visited:
            t += 1
            d_visited[i] = (i, t)
            continue
        if i not in d_visited:
            s = i
            #DFS(dic, i)
            DFS_iter(dic, i)
    #print 25, d_visited

stack_op = 0
   
def DFS_iter(dic,v):
    global d_visited
    global t
    global s
    global stack_op
    stack = []
    stack.append(v)
    stack_op += 1
    stack_helper = {} # Use dic to speed up "is in" op: O(1) VS O(n)
    #print 155, stack
    while stack != []:
        v = stack[-1]
        #temp_n = len(stack)
        has_add = False
        if v not in d_visited:
            #d_visited[v] = s
            d_visited[v] = (s, 0)
            if v in dic:
                #for j in dic[v]:
                temp = dic[v]
                for k in range(len(temp)-1, -1, -1):
                    j = temp[k]
                    if j not in stack_helper and j not in d_visited:                    
                        stack.append(j)
                        stack_helper[j] = 0
                        stack_op += 1
                        has_add = True
                        j2 = j
        '''
        found = False
        if v in dic:
            for k in dic[v]:
                if k in stack_helper and k not in d_visited:
                    found = True # more in the chain to explore
                    k2 = k
                    break
        if found != has_add:
            print 212, k2, j2, found, has_add
            return 
            #print 196
        
        if found and has_add:
        '''
        if has_add:
            #print 171, (s, t), stack
            #print 172, d_visited
            continue
        
        t += 1
        #if v not in d_visited or isinstance(d_visited[v], int):
        if v not in d_visited:
            d_visited[v] = (s, t)
            stack.pop(-1)
        else:
            (a, b) = d_visited[v]
            if b == 0:
                d_visited[v] = (s, t)
                stack.pop(-1)
        #print 163, (s, t), stack
        #print 164, d_visited

def DFS_tail(dic, i, done = False, to_visit = []):
    # ???
    global d_visited
    global t
    global s # leader
    d_visited[i] = s
    #print 74, i, s, t, d_visited
    #print 109, i, dic
    
    if done and to_visit == []:
        t += 1
        d_visited[i] = (s, t)
        return 
        
    if i in dic:
    #    return
    #else:
        for j in dic[i]:
            if j in d_visited:
                if j in to_visit:
                    to_visit.remove(j)
                #return 
                
            if j not in d_visited:
                to_visit += [j]
                DFS_tail(dic, j, done, to_visit)
    
    
def DFS(dic, i):
    global d_visited
    global t
    global s # leader
    d_visited[i] = s
    #print 74, i, s, t, d_visited
    #print 109, i, dic
    
    if i in dic:
    #    return
    #else:
        for j in dic[i]:
            if j not in d_visited:
                DFS(dic, j)
    t += 1
    d_visited[i] = (s, t)
    #print 37, i, s, t, d_visited
    #print 38, dic


'''
dic = load_data()
print 75, dic
dic_r = get_Grev(dic)
print 77, dic_r
'''

master()

print(time.time() - start_time)
print(stack_op)

'''
t = 0
s = 9
d_visited = {}
DFS(dic, 9)
'''
