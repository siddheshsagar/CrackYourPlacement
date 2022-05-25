# Leetcode Problem 11. Container With Most Water
# Problem link : https://leetcode.com/problems/container-with-most-water/

def maxArea(self, height: List[int]) -> int:
        Max = 0
        l = 0
        r = len(height)-1
        while l<r:
            Sum = (r-l) * min(height[l],height[r])
            if Sum > Max:
                Max = Sum
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return Max
