def choose_pivot1(nums):
    #return nums[0]
    return 0

def choose_pivot2(nums):
    #return nums[-1]
    return -1

def choose_pivot3(nums):
    first = nums[0]
    last = nums[-1]
    if len(nums) % 2 == 0:
        mid = nums[len(nums)/2-1]
    else:
        mid = nums[len(nums)/2]
    pivot = (first + mid + last) - max(first, mid, last) - min(first, mid, last)
    if pivot == first:
        return 0
    elif pivot == last:
        return len(nums) - 1
    elif len(nums) % 2 == 0:
        return len(nums)/2 - 1
    else:
        return len(nums)/2
    
def partition1(nums, lo, hi):
    # Pick the 1st element
    #p = choose_pivot1(nums[lo:hi+1])
    p = lo
    #print nums, p
    i = lo + 1
    #j = 0
    for j in range(i,hi+1):
        #print 'a', nums, j, p
        if nums[j] < nums[p]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        #j += 1
    #print 'b', nums, p, i
    nums[p], nums[i-1] = nums[i-1], nums[p]
    #print 'c', nums, nums[p], p
    return i-1
    #return nums

def partition2(nums, lo, hi):
    # Pick the last element
    #p = choose_pivot1(nums[lo:hi+1])
    p = hi
    #print nums, p
    i = lo
    #j = 0
    for j in range(lo, hi+1, 1):
        #print 'a', nums, j, p
        if nums[j] < nums[p]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        #j += 1
    #print 'b', nums, p, i
    nums[p], nums[i] = nums[i], nums[p]
    #print 'c', nums, nums[p], p
    return i
    #return nums
        
def quick_sort(nums, lo, hi, op):
    #print 65, nums, lo, hi
    #if hi - lo <= 0:        
    # return 0
    c1, c2, c3, c4, c = 0, 0, 0, 0, 0
    if lo < hi:
        if op == 1:
            p = partition1(nums, lo, hi)
        elif op == 2:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            p = partition1(nums, lo, hi)
        elif op == 3:
            p = choose_pivot3(nums)
            nums[lo], nums[p] = nums[p], nums[lo]
            p = partition1(nums, lo, hi)
        #print 70, p, lo, hi
        c1 = quick_sort(nums, lo, p - 1, op)
        c3 = (p-1) - lo
        c2 = quick_sort(nums, p + 1, hi, op)
        #print 78, nums, p, lo, hi
        c4 = hi - (p+1)
        c = hi - lo + 1
        # each quick_sort call has a (lo, hi) comparison
        c1 += 1
        c2 += 1
        '''
        c1 = max(c1, 0)
        c2 = max(c2, 0)
        c3 = max(c3, 0)
        c4 = max(c4, 0)
        
        c1 = abs(c1)
        c2 = abs(c2)
        c3 = abs(c3)
        c4 = abs(c4)
        '''
        #print c1, c2, c3, c4, nums, lo, hi, c
    return c1 + c2 + c3 + c4

test1 = [9,8,7,6,5,4,3,2,1, 11, 15,14,13,12,9,7,5,22]
test2 = [9,8]

test10 = [3,9,8,4,6,10,2,5,7,1]

file_name = 'hw2_test1000.txt' #'QuickSort.txt'
lines = [line.strip('\r\n') for line in open(file_name)]
lines = [int(line) for line in lines]
test =  lines[:]
#test = test2
#print 'v1', quick_sort(test, 0, len(test) - 1, 1)
#print test
test = lines[:]
print 'v2', quick_sort(test, 0, len(test) - 1, 3)
print test[:50]

                                  
