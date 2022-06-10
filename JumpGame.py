# Leetcode Problem 55. Jump Game
# Problem linnk : https://leetcode.com/problems/jump-game/

def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return 1
        
        if nums[0] == 0:
            return 0
        
        dp = [0]*len(nums)
        dp[0] = 1
        
        for i in range(len(nums)-1):
            if (i + nums[i]) < len(nums):
                for j in range(i+1,i + nums[i] + 1):
                    if dp[j] == 0:
                        dp[j] = 1
            else:
                if all(dp[:i+1]):
                    return 1
                else:
                    return 0
                
        return all(dp)
