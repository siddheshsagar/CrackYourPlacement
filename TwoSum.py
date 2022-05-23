# Leetcode Problem 1. Two Sum
# Problem Link : https://leetcode.com/problems/two-sum/

def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
        if target - nums[i] in dic:
            return [dic[target - nums[i]], i]
        dic[nums[i]] = i
