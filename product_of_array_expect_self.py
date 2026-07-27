def product_expect_self(num):
    n=len(num)
    answer=[1]*n
    prefix=1
    for i in range(n):
        answer[i]=prefix
        prefix*=num[i]

    safix=1
    for i in range(n-1,-1,-1):
        answer[i]*=safix
        safix*=num[i]

    return answer
num=[1,2,3,4]
print(product_expect_self(num))    
