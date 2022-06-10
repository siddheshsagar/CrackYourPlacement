Leetcode Problem 169. Majority Element
Problem Link : https://leetcode.com/problems/majority-element/



def majorityElement(self, nums: List[int]) -> int:
        dic = dict()
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
          
        res = 0
        maxi = 0
        for i,j in dic.items():
            if maxi < j:
                maxi = j
                res = i
        return res
        
        
################ OR #####################

def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
