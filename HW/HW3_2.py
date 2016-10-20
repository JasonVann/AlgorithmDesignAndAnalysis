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
        v = random.choice(dic.keys())
        if u != v and v in dic[u]:
            return (u, v)

    print 41, 'Not here'
    left_vertices = dic.keys()
    #u = random.randint(1, len(left_vertices) - 1)
    all_keys = []
    for key in dic.keys():
        if isinstance(key, tuple):
            all_keys += list(key)
        else:
            all_keys += [key]
        
    found = False
    while True:
        u = random.choice(all_keys)
        #v = random.randint(1, len(left_vertices) - 1)
        v = random.choice(all_keys)
        #print 27, dic, u, v
        '''
        if u != v:
            #Then make sure u and v are connected directly
            for key, val in dic.items():
                if u in key and v in val:
                    break
            #if v in dic[u]:
            #    break
        '''
        break
    return (u, v)

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
                '''
                val2 = dic2[key]
                dic2.pop(key)
                val2.remove(v)
                key2 = tuple(list(key)+[v])
                dic2[key2] = val2
                dic2.pop(v)
                '''
        print 64, dic2, (u, v)
     
        #break
        dic = dic2
        if len(dic) == 2:
            print 96, dic2
            break
            
def master():
    #Call multiple times
    
    dic = load_data()
    n = len(dic)
    cur = -1
    print 68, dic
    #for i in range(int(n**1*math.log(n))):
    for i in range(1):    
        dic2 = dict(dic)
        rand_contract(dic2)
        #for key, val in temp.items():
        #count = len(val)
        
        count = len(dic2.values()[0])
        #count = len(dic2)
        print 165, cur, dic2
        if cur == -1 or count < cur:
            cur = count
            
    print 67, dic, dic2, cur
    
def load_data():
    file_name = "HW3_Test1.txt"
    lines = [line.strip("\r\n") for line in open(file_name)]
    
    dic = {}
    for line in lines:
        if len(line) > 0:
            a = line[1:].strip().split(' ')
            a = [int(b) for b in a]
            dic[int(line[0])] = a
    print dic
    return dic

dic = load_data()
#print rand_two(dic)
#dic2 = rand_contract(dic)

master()
