def twosum(num,target):
    left=0
    right=len(num)-1
    while left<right:
        total=num[left]+num[right]

        if total==target:
            return[left+1,right+1]
        else-if tota