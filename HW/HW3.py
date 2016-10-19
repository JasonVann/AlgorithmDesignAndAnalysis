import random

def rand_two(left_vertices,arr):
    u = random.randint(1, len(left_vertices) - 1)
    while True:
        v = random.randint(1, len(left_vertices) - 1)
        if u != v:
            #Then make sure u and v are connected directly
            res = [k for k in arr if u in k and v in k]
            if len(res) > 0:
                break
    return (u, v)

def rand_contract(arr):
    visited = []
    #for i in range(len(all)):
    left_vertices = [k[0] for k in arr]
    while True:
        (u, v) = rand_two(left_vertices, arr)
        
        if len(all) == 2:
            break

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

load_data()
