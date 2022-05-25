# Leetcode Problem 15. 3Sum
# Problem Link : https://leetcode.com/problems/3sum/

def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = list()
        nums.sort()
        for i in range(len(nums) - 2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    if [nums[i],nums[j],nums[k]] not in arr:
                        arr.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return arr
