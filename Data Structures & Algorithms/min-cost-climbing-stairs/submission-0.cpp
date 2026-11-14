#include <limits.h>
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        for (int i= cost.size()-2; i>=0; i--){
            int lm = INT_MAX;
            if (i+2 == cost.size()){
                lm = min(cost[i]+cost[i+1], cost[i]);
            }
            else{
                lm = min(cost[i]+cost[i+1], cost[i]+cost[i+2]);
            }
            cost[i]=lm;
        }
        return min(cost[0], cost[1]);
    }
};
