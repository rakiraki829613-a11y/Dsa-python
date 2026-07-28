def sor(num,target):
    
    left=0
    right=len(num)-1
    
    while left<=right:
        mid=(left+right)//2
        if num[mid]==target:
         return mid
        if num[left]<=num[mid]:
          if num[left]<=target<num[mid]:
             right=mid-1
          else:
             left=mid+1

        else:
           if num[mid]<target<=num[right]:
             left=mid+1
           else:
            right=mid-1
    return -1
num=[4,5,6,7,0,1,2]
target=6
print(sor(num,target))
    
    