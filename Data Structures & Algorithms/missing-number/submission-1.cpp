class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int x=0;
        int n= nums.size();
        for (int i=0; i<n; i++){
            x+=nums[i];
        }
        int sum = n*(n+1)/2;
        if (x==sum){
            return 0;
        }
        return sum-x;
    }
};
