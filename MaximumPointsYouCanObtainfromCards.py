# leetcode Problem 1423. Maximum Points You Can Obtain from Cards
# Problem Link : https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

def maxScore(self, cardPoints: List[int], k: int) -> int:
        lis1 = [0]*len(cardPoints)
        lis2 = [0]*len(cardPoints)
        sum1 = 0
        sum2 = 0
        i = 0
        j = len(cardPoints)-1
        while i < len(cardPoints):
            sum1 += cardPoints[i]
            lis1[i] = sum1
            i += 1
            
        while j >= 0:
            sum2 += cardPoints[j]
            lis2[j] = sum2
            j -= 1
        lis2.append(0)
        lis1.insert(0,0)
        
        res = cardPoints[:len(cardPoints)-k]
        final = 0
        i = 0
        j = len(cardPoints)-k
        while j < len(cardPoints)+1:
            temp = lis1[i] + lis2[j]
            if final < temp:
                final = temp
            i += 1
            j += 1
        return final
