def remove_elements(nums,val):
    k=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[i]==nums[k]
            k+=1
    return k
nums=[1,2,2,3,4,5]
val=1
print(remove_elements(nums,val))