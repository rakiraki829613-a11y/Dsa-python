def maximum_subarray_sum(num):
    curent_sum=num[0]
    maximum_sum=num[0]

    for i in range(1,len(num)):
        curent_sum=max(num[0],curent_sum+num[0])
        maximum_sum=max(curent_sum,maximum_sum)
    return maximum_sum
num=[1,2,3,4]
print(maximum_subarray_sum(num))    