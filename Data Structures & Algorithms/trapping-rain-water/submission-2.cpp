class Solution {
public:
    int trap(vector<int>& height) {
        int maxh= 0;
        for (int i=0; i<height.size(); i++){
            if (height[i]>maxh) maxh= height[i];
        }
        vector<vector<int>> dp(maxh, vector<int>(height.size(), 0));
        int state= 0; //0 means didn't start, 1 means 1 found
        for (int i=0; i<height.size(); i++){
            for (int j=maxh-1; j>maxh-1-height[i]; j--){
                dp[j][i]= 1;
            }    
        }
        int v=0; 
        for (int i=0; i<maxh; i++){
            state=0;
            int count=0;
            for (int j=0; j<height.size(); j++){
                if (dp[i][j]==1){
                    switch (state){
                        case 0: count=0; state=1; break;
                        case 1: v=v+count; count=0; state=1; break;
                        default: break;
                    }
                }
                else{
                    count++;
                }
            }
        }
        return v;
    }
};
