def getConcatenation(nums):
    ans = []

    for i in range(len(nums)):
        ans.append(nums[i])

    for i in range(len(nums)):
        ans.append(nums[i])

    return ans


# Example
nums = [1, 2, 1]
print(getConcatenation(nums))