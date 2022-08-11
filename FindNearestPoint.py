# Leetcode Problem 1779 : 1779. Find Nearest Point That Has the Same X or Y Coordinate
# Problem link : https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
    p1,p2,min_mhd = 0,0,maxsize
    for i,j in points:
        if i == x or j == y:
            mhd = abs(x-i) + abs(y-j)
            if mhd < min_mhd:
                p1 = i
                p2 = j
                min_mhd = mhd
    return points.index([p1,p2]) if p1 and p2 else -1
  
  
'''
  Expanding return points.index([p1,p2]) if p1 and p2 else -1 for better understanding =>

	if (p1 != 0 and p2 != 0):
		return points.index([p1,p2])
	else:
		return -1
```
