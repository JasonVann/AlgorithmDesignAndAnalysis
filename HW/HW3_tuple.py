import random
import math

# This version uses tuple as values stored in dictionary and keeps the history of merging; which is more complext than necessary

rand_count = 0
#rand_all = [(1, 3), (8, 7), (5, 4), (8, 5), (6, 8), (2, 1)]
rand_all = [(1, 2), (1, 3), (1, 4), (7, 6), (7, 8), (7, 5)]
rand_all = [(8, 7), (5, 7), (5, 4),(3,1), (1,7), (6,5), (8,2)]
rand_all = [(1,2), (3,4), (7,1), (6, 5), (2, 4)]

def rand_two(dic):
    
    global rand_count, rand_all
    (u, v) = rand_all[rand_count]
    rand_count += 1
    return (u, v)
    '''
    
    while True:
        u = random.choice(dic.keys())
        v = random.choice(dic.keys())
        #print 18, u, v, dic
        if u != v:
            (u1, u2) = dic[u]
            (v1, v2) = dic[v]
            #if u1 != [0] and v1 != [0] and v in u2:
            if v in u2: #?? fail when n is large
                break
    '''
    '''
    while True:
        u = random.choice(dic.keys())
        (u1, u2) = dic[u]
        if u2 != []:
            v = random.choice(u2)        
            break
    '''            
    return (u, v)        
        
def rand_contract(dic):
    dic_absorbed = {}
    l_absorbed = []
    test_count = 0
    while True:
        (u, v) = rand_two(dic)
        
        print 43, (u, v)
        #print 21, dic[v]
        (v1, v2) = dic[v]
        (u1, u2) = dic[u]

        
        #if u == 5:
        #print 50, u, v, dic[u], dic[v]
        
        if u1 == [0]:
            u, v = v, u
        (v1, v2) = dic[v]
        (u1, u2) = dic[u]

        u_head = -1
        v_head = -1
        if v1 == [0]:
            v2.remove(u)
            for key, val in dic.items():
                (a, b) = val
                if v in a:
                    #Then we find the real absorber u
                    v_head = key
                    #u, v = key, u
                if u1 == [0] and u in a:
                    u_head = key
                    
                    #a.append(u)
                    #b = list(set(set(b) + set(v2) - set([u])))
        u0, v0 = u, v
        #u = u_head
        #v = v_head
        if u_head != -1:
            if v in u2:
                u2.remove(v)
            
        (v1, v2) = dic[v]
        (u1, u2) = dic[u]
        print 68, (u, v)
        if v1 == []:
            v1 = [0]
            dic[v] = (v1, v2)
                    
        else:
            #v is already a cluster
            if (u, v) == (8, 3):
                print 76, u, v, dic
            u1 += v1
            print 78, u1, v1, dic
            #u2 += v2
            #u2 = list(set(u2))

            if v in u2:
                u2.remove(v)
            if u in u2:
                u2.remove(u)
            if u in v2:
                v2.remove(u)
            dic[v] = ([0], v2)
            #print 88, (u, v), dic #dic[u], dic[v]
        #print 23, dic[v]
        
        if u in v2:
            v2.remove(u)
        if v not in u1:
            u1 += [v]
        print 96, (u, v), dic
        for i in u1:
            if i in v2:
                v2.remove(i)
            if i in u2:
                u2.remove(i)
            
            if i != 0:
                (a, b) = dic[i]
                if v in b:
                    b.remove(v)
                
                    b = list(set(b) - set(u1))
                    #print 59, b, dic[i]
                    dic[i] = (a,b)
        dic4 = dict(dic)
        u11 = u1[:]
        for i in u1:
            (a, b) = dic[i]
            b2 = b[:]
            for j in b:
                if j in u1:
                   b2.remove(j)
            dic[i] = (a, b2)
        #dic[u] = (u11, u2)
        
        if v in u2:
            u2.remove(v)
        if u in u2:
            u2.remove(u)
        #print 55, u1, u2, dic[u], dic[v]
        #print 56, u, v, dic[u], dic
        dic[u] = (u1,u2)
        #print 33, dic[u]
        #print 34, dic[u], dic
        print 132, dic
        test_count += 1
        if test_count >= 100:
            break
        l_absorbed += [v]
        print 136, (u, v), dic, l_absorbed
        if len(dic) - len(l_absorbed) == 2:
            break
    #print 94, dic
    # Then consolidate
    dic3 = dict(dic)
    g1 = []
    g2 = []
    
    #print 82, dic, l_absorbed
    for key, val in dic3.items():
        (a, b) = val
        if a != [0]:
            g1 = [key] + a
            break
    res = []
    for k in g1:
        (a, b) = dic[k]
        if b != []:
            res += b
    print 155, dic
    print 113, g1, res
    return len(res)

    #print 85, g1, dic3[g1[0]]
    (a, b) = dic3[g1[0]]
    res1 = []
    #print 104, g1, (a,b), dic3
    for k1 in a:
        if k1 != 0:
            (a1, b1) = dic3[k1]
            res1 += b1
    res1 += b
    res = list(set(res1) - set(a) - set([g1[0]]))
    #print 95, res, res1, b, a, g1[0]
    '''
    (a, b) = dic3[g1[1]]
    res2 = []
    for k1 in a:
        (a1, b1) = dic3[k1]
        res2 += b1
    res2 += b
    res = list(set(res1) - set(a))
    '''
    if len(res) == 0:
        print 122, dic, res, res1, g1
    return len(res)
    '''
    dic3[g1[0]] = (a, res1)
    print 91, dic3, res1
    dic3[g1[0]] = list(set(dic3[g1[0]]))
    for k1 in dic3[g1[1]]:
        dic3[g1[1]] += dic3[k1]
    dic3[g1[1]] = list(set(dic3[g1[1]]))
    print 92, dic3
    
        
    return dic
    '''
    
def master():
    #Call multiple times
    
    dic0 = load_data()
    n = len(dic0)
    cur = -1
    print 68, dic0
    for i in range(int(n**1*math.log(n))):
    #for i in range(1):  
        dic0 = load_data()
        dic02 = dict.copy(dic0)
        #print 145, dic02
        # ????
        #print 146, dic0 is dic02, dic0
        temp = rand_contract(dic02)
        #print 149, dic0
        #for key, val in temp.items():
        #count = len(val)
        count = temp
        '''
        for key, val in temp.items():
            (a, b) = val
            if b != []:
                count += 1
        '''
        print 221, cur, count
        if cur == -1 or count < cur:
            cur = count
            
    print 67, dic0, dic02, cur
    
def load_data():
    file_name = "HW3_Test1.txt"
    lines = [line.strip("\r\n") for line in open(file_name)]
    
    dic = {}
    for line in lines:
        if len(line) > 0:
            line = line.strip().split(' ')
            #print 155, line, 'line0=', line[0], line[1:]
            #a = line[1:].strip().split(' ')
            a = line[1:]
            a2 = [int(b) for b in a]
            #print 158, a, a2
            dic[int(line[0])] = ([], a2)
            #print 159, dic[int(line[0])]
    #print 161, dic
    #print 50, rand_two(dic)
    return dic

#dic = load_data()
#print rand_contract(dic)
master()
