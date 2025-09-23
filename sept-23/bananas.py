def minEatingSpeed(piles, h)

    def time_taken(rate):
        total = 0
        for pile in piles:
            total += (pile + rate - 1) // rate
        
        return total
    
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        total_time = time_taken(mid)
        if total_time > h:
            left = mid + 1
        else:
            right = mid

    return left