# Leetcode Problem 560. Subarray Sum Equals K
# Problem Link : https://leetcode.com/problems/subarray-sum-equals-k/

# Time Complexity : O(n)
# Space Complexity : O(n)
 def subarraySum(self, nums: List[int], k: int) -> int:
        dic = dict()
        dic[0] = 1
        sum1 = 0
        cnt = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            if sum1 - k in dic:
                cnt += dic[sum1-k]
            if sum1 in dic:
                dic[sum1] += 1
            else:
                dic[sum1] = 1
        return cnt
