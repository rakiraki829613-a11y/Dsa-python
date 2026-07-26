def duplicate_elements(s):
    seen=set()
    for nums in s:
        if nums in seen:
            return True
        seen.add(nums)
    return False
s=[1,2,3,11]
print(duplicate_elements(s))

        