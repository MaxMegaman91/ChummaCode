import timeit

start = timeit.default_timer()

#####################################################

"""def findMax(nums, minK, maxK):
    def possibilities(nums, leng=1):
        returnval = 0
        if leng==len(nums) + 1: return 0
        for x in range(len(nums)-(leng-1)):
            y = nums[x:x+leng]
            if min(y) == minK and max(y) == maxK: returnval += 1
        return returnval + possibilities(nums, leng+1)

    return possibilities(nums)"""

def findMax(nums, k):
    sp = 0
    sum = 0
    keyval = {}

    for x in range(len(nums)-k+1):
        if nums[x] in keyval:
            keyval[nums[x]] = 1
        else:
            keyval[nums[sp]] = None
            sp += 1

        
print(findMax(nums = [1,5,4,2,9,9,9], k = 3))
#####################################################
stop = timeit.default_timer()

print('Time: ', stop - start) 

