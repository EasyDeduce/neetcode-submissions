class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int x=0;
        int n= nums.size();
        int y=n;
        for (int i=0; i<n; i++){
            x^=nums[i];
            y^=i;
        }   
        return x^y;
    }
};
