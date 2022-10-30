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

def findMax(creators, ids, views):
    return
        
print(findMax(creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]))
#####################################################
stop = timeit.default_timer()

print('Time: ', stop - start) 

