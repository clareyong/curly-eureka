def lcs(text1, text2):

    if len(text1) < len(text2):
        text1, text2 = text2, text1
    dp = [0] * (len(text1) + 1)

    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] == text2[j]:
                dp[i+1] = dp[i] + 1
            else:
                dp[i+1] = max(dp[i], dp[i+1])
        print(dp)
    return dp[len(text1)]

text1 = "oxcpqrsvwf"
text2 = "shmtulqvypy"

# text1 = "abcde"
# text2 = "ace"

# text1 = "vozsh"
# text2 = "psnw"

print(lcs(text1, text2))
