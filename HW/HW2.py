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
        
def quick_sort(nums, lo, hi):
    #if len(nums) <= 1:
    #    return nums
    if lo < hi:
        p = partition1(nums, lo, hi)
        quick_sort(nums, lo, p - 1)
        quick_sort(nums, p + 1, hi)
    return nums

test1 = [9,8,7,6,5,4,3,2,1, 11, 15,14,13,12,9,7,5,22]
test2 = [9]

lines = [line.strip('\r\n') for line in open('QuickSort.txt')]
lines = [int(line) for line in lines]
test = lines
#print test[:50]
print quick_sort(test, 0, len(test) - 1)
                                  
