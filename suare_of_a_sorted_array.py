def sorted_sures(nums):
    nums=sorted(nums)
    n=len(nums)
    result=[0]*n

    left=0
    rigth=n-1

    for i in range(n-1,-1,-1):
        if abs(nums[left])>abs(nums[rigth]):
            result[i]=nums[left]*nums[left]
            left+=1
        else:
            result[i]=nums[rigth]*nums[rigth]
            rigth-=1
    return result
nums=[1,-4,3,2]
print(sorted_sures(nums))            
