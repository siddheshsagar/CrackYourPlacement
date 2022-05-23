# Leetcode Problem 121. Best Time to Buy and Sell Stock
# Problem Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Python Code
def maxProfit(self, prices: List[int]) -> int:
        right_side=1
        max_pr = 0
        
        size = len(prices)

        buy_price = prices[0] # 7 
        while right_side < size:
            
            if buy_price <= prices[right_side]:
                diff = prices[right_side] - buy_price
                max_pr = max(max_pr, diff )
                
            else:
                buy_price = prices[right_side]
                
            right_side+=1
        
        return max_pr
 


# C++ Code
int maxProfit(vector<int>& prices) 
{
    int mi=INT_MAX,ans=0;
    for(int i=0;i<prices.size();i++)
    {
        mi=min(mi,prices[i]);
        ans=max(ans,prices[i]-mi);
    }
    return ans;
}
