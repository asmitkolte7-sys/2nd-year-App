# Climbing Stairs Problem using Dynamic Programming

def climb_stairs(n):
    # Base cases
    if n <= 2:
        return n

    # DP table to store results
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    # Bottom-up calculation
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# -------- Main Program --------
n = int(input("Enter number of stairs: "))
ways = climb_stairs(n)
print(f"Total number of distinct ways to climb {n} stairs: {ways}")




#OUTPUT

Enter number of stairs: 5
Total number of distinct ways to climb 5 stairs: 8
