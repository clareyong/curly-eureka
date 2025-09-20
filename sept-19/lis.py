def lengthOfLIS(self, nums: List[int]) -> int:
    result=[1] * (len(nums)+1)

    result[0] = 0
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                result[i+1] = max(result[i+1], (result[j+1] + 1))
    return max(result)