def container_with_most_water(heigth):
    left=0
    right=len(heigth)-1
    max_water=0
    while left<right:
        width=right-left
        water=min(heigth[left],heigth[right])*width
        max_water=max(water,max_water)


        if heigth[left]<heigth[right]:
            left +=1
        else:
            right -=1

    return max_water
heigth=[1,8,6,2,5,4,8,3,7]
print(container_with_most_water(heigth))