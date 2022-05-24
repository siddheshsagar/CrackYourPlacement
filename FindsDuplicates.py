# Leetcode Problem 442. Find All Duplicates in an Array
# Problem Link : https://leetcode.com/problems/find-all-duplicates-in-an-array/

def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = dict()
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        res = []
        for i,j in dic.items():
            if j == 2:
                res.append(i)
        return res
