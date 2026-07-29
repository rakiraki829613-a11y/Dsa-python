def remove_sorted_array(nums):
    k=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[i]==nums[k]
            k+=1
    return k
nums=[1,1,2,2,3,4,5]
print(remove_sorted_array(nums))        
