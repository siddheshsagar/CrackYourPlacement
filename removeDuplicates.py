# Leetcode problem 26. Remove Duplicates from Sorted Array

# I am using extra space here which is not suggested
# try to solve it in linear time and O(1) extra space

def removeDuplicates(self, nums: List[int]) -> int:
        lis = []
        arr = [i for i in nums]
        j = 0
        for i in range(len(arr)):
            if arr[i] not in lis:
                lis.append(arr[i])
                nums.insert(j,arr[i])
                j += 1
                
        return j
