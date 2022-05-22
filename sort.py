# Leetcode problem 75. Sort Colors

def sortColors(self, nums: List[int]) -> None:
        a = nums.count(0)
        b = nums.count(1)
        c = nums.count(2)
        for i in range(a):
            nums[i] = 0
        for i in range(a,a+b):
            nums[i] = 1
        for i in range(a+b,a+b+c):
            nums[i] = 2
        return nums
