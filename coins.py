class solution(object):
    def coinchange(self,coins,amount):
        coins=[1,2,5]
        amount=11
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for amt in range(1,amount+1):
            for c in coins:
                if amt-c>0:
                    dp[amt]=min(dp[amt],dp[amt-c]+1)
    return dp[amount] if dp[amount]<=amount else -1
