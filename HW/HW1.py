def merge_count(A1, B1):
    i, j = 0, 0
    sorted = []
    count = 0
    while i < len(A1) and j < len(B1):
        if A1[i] <= B1[j]:
            sorted.append(A1[i])
            i += 1
        else:
            sorted.append(B1[j])
            j += 1
            count += len(A1) - i
    #print i, j, sorted, count
    if j <= len(B1) - 1:
        sorted += B1[j:]
    if i <= len(A1) - 1:
        sorted += A1[i:]
        #count += len(A1) - i - 1
    
    return (sorted, count)

A1 = [1,3,5]
B1 = [2,4,6,8]
print merge_count(A1, B1)

            
        
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    A = lst[:len(lst)/2]
    B = lst[len(lst)/2 :]
    A1 = merge_sort(A)
    B1 = merge_sort(B)
    (sorted, count) = merge_count(A1, B1)
    return sorted

print merge_sort([1,3,2,0,-1,4,-2,10,9,8,7])


def count_inversion(lst):
    if len(lst) <= 1:
        return (lst, 0)
    A = lst[:len(lst)/2]
    B = lst[len(lst)/2:]
    (A1,c1) = count_inversion(A)
    (B1,c2) = count_inversion(B)
    (sorted, count) = merge_count(A1, B1)
    
    return (sorted, c1+c2+count)

test1 = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]

#f = open('IntegerArray.txt', 'r')

#test1 = f.read()
lines = [line.rstrip('\r\n') for line in open('IntegerArray.txt')]
lines = [int(line) for line in lines]
print lines[:50]
(sorted, c) = count_inversion(lines)
print c;
print sorted[:30]
