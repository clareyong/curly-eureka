apples = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]

def can_reach(time, distance):
    if distance <= time:
        return True
    return False

def calc_distance(x1,y1, x2, y2):
    x = (x1 - x2) * (x1 - x2)
    y = (y1 - y2) * (y1 - y2)
    d = (x + y) ** 0.5
    return d

def catch_apples(apples):

    dp = [0] * (len(apples) + 1)
    dp[1] = 1
    for i in range(1, len(apples)):
        t1,x1,y1 = apples[i-1][0], apples[i-1][1], apples[i-1][2]
        t2,x2,y2 = apples[i][0], apples[i][1], apples[i][2]
        distance = calc_distance(x1,y1,x2,y2)
        reach = can_reach(t2-t1, distance)
        print(distance, (t2-t1), reach)
        dp[i+1] = (dp[i] + reach)
    print(dp)
    return dp[len(apples)]

apples = [(2,2,0), (4,10,0), (6,6,0)]
print(catch_apples(apples))