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

def findMax(nums, minK, maxK):
    returnval = 0
    for leng in range(1,len(nums)+1):
        for x in range(len(nums)-(leng-1)):
            if min(nums[x:x+leng]) == minK and max(nums[x:x+leng]) == maxK: 
                returnval += 1

    return returnval


print(findMax(nums = [1,1,1,1], minK = 1, maxK = 1))
        

#####################################################
stop = timeit.default_timer()

print('Time: ', stop - start) 

