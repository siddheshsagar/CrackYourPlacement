# Leetcode question 283. Move Zeroes
# Problem Link : https://leetcode.com/problems/move-zeroes/

def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) > 1:
            cnt = 0
            n = len(nums)
            for i in range(n):
                if nums[i] == 0:
                    nums.append(0)
                    cnt+=1
            # print(cnt)
            # print(nums)
            while cnt > 0:
                nums.remove(0)
                cnt -= 1
