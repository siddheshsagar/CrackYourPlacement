# Chocolate Distribution Problem - GeeksForGeeks
# Problem Link : https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1#

def findMinDiff(self, arr,N,M):
        arr.sort()
        mini = 10000000000
        j = 0
        for i in range(M-1,N):
            if arr[i] - arr[j] < mini:
                mini = arr[i] - arr[j]
            j += 1
            
        return mini
