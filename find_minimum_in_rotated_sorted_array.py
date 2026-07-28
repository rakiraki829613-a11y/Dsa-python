def sorteedsortarray(num):
    n=len(num)
    left=0
    right=n-1
    mid=(left+right)//2
    while left<right:
        if num[mid]<num[right]:
            left=mid+1
        else:
            right=mid

    return num[left] 
num=[1,2,3,4,0]
print(sorteedsortarray(num))           