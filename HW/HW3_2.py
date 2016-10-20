import random
import math

rand_all = [(3,2), (4,5), (1,7), (4,8), (1, 6), (1,4)]
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
    while True:
        (u, v) = rand_two(dic2)
        #v is absorbed by u
        #(u, v) = (1,2)
        #dic2 = dict(dic)
        #dic2[v].remove(u)
        dic2[v] = [x for x in dic2[v] if x != u]
        dic2[u] += (dic2[v])
        #dic2[u].remove(v)
        dic2[u] = [x for x in dic2[u] if x != v]
        dic2.pop(v)
        #print 51, (u, v), dic2
        for key, val in dic2.items():
            if v in val:
                val2 = [u if e == v else e for e in val]
                #val.remove(v)
                #val.append(u)
                dic2[key] = val2
        #print 64, dic2, (u, v)
     
        #break

        dic = dic2
        if len(dic) == 2:
            #print 96, dic2
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
    #for i in range(1):
        dic = load_data()
        #print 66, dic
        dic2 = dict(dic)
        rand_contract(dic2)
        #for key, val in temp.items():
        #count = len(val)
        #print 71, dic2 is dic, dic
        #print 72, dic2
        count = len(dic2.values()[0])
        #count = len(dic2)
        #print 165, cur, dic2
        res += [count]
        if cur == -1 or count < cur:
            cur = count
            
    print 67, dic, dic2, cur

def load_data():
    #file_name = "kargerMinCut.txt" # "HW3_Test3.txt"
    file_name = "HW3_Test3.txt"
    lines = [line.strip("\r\n") for line in open(file_name)]
    
    dic = {}
    for line in lines:
        if len(line) > 0:
            #line = line.strip().split('\t')
            line = line.strip().split(' ')
            print 155, line, 'line0=', line[0], line[1:]
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
print dic
#print rand_two(dic)
#dic2 = rand_contract(dic)

import datetime
import time
print 'start', datetime.datetime.now()

start_time = time.time()

#master()
print datetime.datetime.now()
print time.time() - start_time
