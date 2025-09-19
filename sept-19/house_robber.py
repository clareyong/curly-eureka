def rob(nums):

    """
    Maximise items to rob - cannot rob adjacent houses

    house = [1,2,3,1,1]
    # haul = [0,1,2,0,0]    

    at the first house, the best haul we can get is 1
    at the second house, we can either take it or not have taken the first house's
    --> max(1,2) = 2
    at the third house, we can either take from house 1 and 3, or just 2 so max(house[3] + haul[1], haul[2])
    """

    haul = [0] * (len(nums) + 1)
    haul[0] = 0

    for i in range(len(nums)):
        haul[i+1] = max(haul[i], (haul[i-1] + nums[i]))
    return haul[len(nums)]

print(rob([1,2,3,1]))