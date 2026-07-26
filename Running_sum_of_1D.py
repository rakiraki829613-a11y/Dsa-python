def runningsun(nums):
    for i in range(1,len(nums)):
        nums[i]=nums[i]+nums[i-1]
    return nums
nums=[1,4,6,8]
print(runningsun(nums))    