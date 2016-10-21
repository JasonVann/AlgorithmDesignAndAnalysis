import random
import math
import copy

rand_all = [(3,2), (4,5), (1,7), (4,8), (1, 6), (4,1)]
rand_count = 0

def rand_two(dic):
    '''
    global rand_count, rand_all
    res = rand_all[rand_count]
    rand_count += 1
    return res
    '''
    
    while True:
        u = random.choice(dic.keys())
        v = random.choice(dic[u])
        if u != v:
            return (u, v)
    '''
    while True:
        u = random.choice(dic.keys())
        
        # maybe too slow if n is large
        v = random.choice(dic.keys())
        #print 18, (u, v), dic
        if u != v and (v in dic[u] or u in dic[v]):
        #if u != v and v in dic[u]:
            return (u, v)
    '''
    
def rand_contract(dic2):
    global dic
    while True:
        (u, v) = rand_two(dic2)
        #v is absorbed by u
        #(u, v) = (1,2)
        '''
        print 38, dic
        print 39, u, v, dic2[u], dic2[v]
        print 40, dic2
        print 41, dic[v], dic[u]
        print 42, dic2[v], dic2[u]
        '''
        dic2[v] = [x for x in dic2[v] if x != u]
        
        #dic2[u] += (dic2[v]) # This fails because dic[u] is dic2[u]
        
        dic2[u] = (dic2[u] + dic2[v])        
        
        dic2[u] = [x for x in dic2[u] if x != v]
        dic2.pop(v)
        for key, val in dic2.items():
            if v in val:
                val2 = [u if e == v else e for e in val]
                
                dic2[key] = val2
                
        if len(dic2) == 2:
            #print 56, dic2
            
            break

res = []
def master():
    #Call multiple times
    global res
    
    dic = load_data()
    n = len(dic)
    cur = -1
    #print 68, dic
    
    for i in range(int(n**2*math.log(n))):
    #for i in range(int(n**2)):
    #for i in range(6):
        global rand_count
        rand_count = 0
        dic2 = copy.deepcopy(dic)
        rand_contract(dic2)
        #print 71, dic
        count = len(dic2.values()[0])
        res += [count]
        if cur == -1 or count < cur:
            cur = count
            
    print 67, cur

def load_data():
    #file_name = "kargerMinCut.txt" # "HW3_Test3.txt"
    file_name = "HW3_Test1.txt"
    lines = [line.strip("\r\n") for line in open(file_name)]
    
    dic = {}
    for line in lines:
        if len(line) > 0:
            line = line.strip().split('\t')
            if len(line) == 1:
                line = line[0].strip().split(' ')
            #line = line.strip().split(' ')
            #print 155, line, 'line0=', line[0], line[1:]
            #a = line[1:].strip().split(' ')
            a = line[1:]
            a2 = [int(b) for b in a]
            #print 158, a, a2
            dic[int(line[0])] = a2
            #print 159, dic[int(line[0])]
    '''
    for line in lines:
        if len(line) > 0:
            a = line[1:].strip().split(' ')
            a = [int(b) for b in a]
            dic[int(line[0])] = a
    '''
    #print dic
    return dic

dic = load_data()

import datetime
import time
print 'start', datetime.datetime.now()

start_time = time.time()

master()
print datetime.datetime.now()
print time.time() - start_time
