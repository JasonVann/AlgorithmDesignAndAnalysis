import time
import copy
from heapq import *

start_time = time.time()

def load_data1():
    file_name = "algo1-programming_prob-2sum.txt"
    lines = [line for line in open(file_name)]
    dic = {}
    count = 0
    for line in lines:
        temp = int(line)
        count += 1
        if temp in dic:
            dic[temp] = dic[temp] + 1
        else:
            dic[temp] = 1
    #print 19, count
    return dic

def cal_2sum():
    dic = load_data1()
    dic_t = {}
    '''
    for i in range(-10000, 10000+1, 1):
        dic_t[i] = 1
    '''
    dic2 = copy.deepcopy(dic)
    for k,v in dic.items():
        for i in range(-100, 100+1, 1):
            if i in dic_t:
                continue
            if i - k != k and (i - k) in dic:
                if (i - k) in dic2:
                    dic2[i - k] = dic2[i - k] - 1
                    if dic2[i - k] == 0:
                        dic2.pop(i - k)
                    dic_t[i] = 1
    print 35, len(dic_t)
    return dic_t
    
def load_data2():
    file_name = "Median.txt"
    lines = [line.strip('\r\n') for line in open(file_name)]
    data = []
    #print lines[:30]
    
    for line in lines:
        temp = int(line)
        data.append(temp)
    return data

    
def median_main():
    data = load_data2()
    #data_neg = [a * (-1) for a in data]
    heap_l = [] # max at top
    heap_h = [] # min at top
    res = []
    data.insert(0, 0)
    for i in range(1, len(data)):
        has_add = False
        if len(heap_l) == 0:
            heap_l.append(-data[i])
            has_add = True
            
        l_max = -heappop(heap_l)
        heappush(heap_l, -l_max)        
        
        if (not has_add) and len(heap_h) == 0 and data[i] > l_max:
            heappush(heap_h, data[i])
            has_add = True
        elif (not has_add) and len(heap_h) == 0 and data[i] <= l_max:
            # Add to left, swap top of left and right
            heappop(heap_l)
            heappush(heap_l, -data[i])
            heappush(heap_h, l_max)
            has_add = True
            
        
        l_max = -heappop(heap_l)
        heappush(heap_l, -l_max)
        if len(heap_h) > 0:
            r_min = heappop(heap_h)
            heappush(heap_h, r_min)
        
        if not has_add and data[i] <= l_max:
            if len(heap_l) - len(heap_h) >= 1:
                l_max = -heappop(heap_l)
                heappush(heap_h, l_max)
                heappush(heap_l, -data[i])
            else:
                heappush(heap_l, -data[i])
        
        if not has_add and data[i] > l_max:
            if len(heap_h) - len(heap_l) >= 1:
                r_min = heappop(heap_h)
                if r_min >= data[i]:
                    heappush(heap_l, -data[i])
                    heappush(heap_h, r_min)
                else:
                    heappush(heap_l, -r_min)
                    heappush(heap_h, data[i])
            else:
                heappush(heap_h, data[i])
        
        l_max = -heappop(heap_l)
        heappush(heap_l, -l_max)
        
        if len(heap_h) > 0:
            r_min = heappop(heap_h)
            heappush(heap_h, r_min)
        
        if i % 2 == 0:
            res.append(l_max)
        else:
            if len(heap_l) == (i+1)/2:
                res.append(l_max)
            else:
                res.append(r_min)
                
    print 87, len(res), sum(res)
    return res
        
            
#dic = load_data1()
dic_t = cal_2sum()

'''
data = load_data2()
res = median_main()
'''

print time.time() - start_time
