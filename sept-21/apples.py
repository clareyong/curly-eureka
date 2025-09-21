def can_reach(apple1,apple2):
    t1,x1,y1 = apple1[0], apple1[1], apple1[2]
    t2,x2,y2 = apple2[0], apple2[1], apple2[2]
    x = (x1 - x2) * (x1 - x2)
    y = (y1 - y2) * (y1 - y2)
    distance = (x + y) ** 0.5
    time = t2 - t1

    if distance <= time:
        return True

    return False

def catch_apples(apples):

    dp = [0] * (len(apples) + 1)
    for i in range(len(apples), -1, -1):
        print(i)
        for j in range(i+1, len(apples)):
            if can_reach(apples[i], apples[j]):
                dp[i] = max(dp[i], dp[j])
        if i >= 0:
            dp[i] += 1
            
    return dp[0]

apples = [(2,2,0), (4,10,0), (6,6,0)]
print(catch_apples(apples))