# Leetcode Problem 18. 4Sum
Problem Link : https://leetcode.com/problems/4sum/

def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                l = j+1
                m = len(nums)-1
                while l < m: 
                    if nums[i]+nums[j]+nums[l]+nums[m] < target:
                        l+=1
                    elif nums[i]+nums[j]+nums[l]+nums[m] > target:
                        m-=1
                    else:
                        if not [nums[i],nums[j],nums[l],nums[m]] in ans:
                            ans.append([nums[i],nums[j],nums[l],nums[m]])
                        l+=1
                        m-=1
        return ans
