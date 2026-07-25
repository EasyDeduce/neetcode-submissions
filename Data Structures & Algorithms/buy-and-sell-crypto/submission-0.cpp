class Solution {
   public:
    int maxProfit(vector<int>& prices) {
        int n= prices.size();
        int profit=-10000;
        for (int i=0; i<n; i++){
            for (int j=i+1; j<n; j++){
                if (profit<prices[j]-prices[i]){
                    profit= prices[j]-prices[i];
                }
            }
        }
        if (profit<0){
            return 0;
        }
        return profit;
    }
};
