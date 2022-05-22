# Leetcode problem 287 -> Find the Duplicate Number

# in linear time  and space we can use dictionary to store the occurances of every 
# element and return the element which occured twice in the dictionary

dic = dict()
for i in range(len(nums)):
    if nums[i] in dic:
        dic[nums[i]] += 1
        if dic[nums[i]] >= 2:
            return nums[i]
    else:
        dic[nums[i]] = 1
