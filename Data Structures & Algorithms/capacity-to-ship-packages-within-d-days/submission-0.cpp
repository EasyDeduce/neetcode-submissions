class Solution {
public:
    int selection(int cap, int days, vector<int> weights){
        int i=0;
        int s=0;
        while (i<weights.size()){
            if (s+weights[i]>cap){
                days-=1;
                s=0;
            }
            s+=weights[i];
            i++;
        }
        days-=1;
        if (days>=0){
            return 1;
        }
        return 0;
    }
    int shipWithinDays(vector<int>& weights, int days) {
        int l = -1;
        int r = 0; 
        for (int i=0; i<weights.size(); i++){
            if (l<weights[i]){
                l=weights[i];
            }
            r+=weights[i];
        }
        while (l<=r){
            int mid = (l+r)/2;
            if  (selection(mid,days,weights)){
                r=mid-1;
            }   
            else{
                l=mid+1;
            }
        }
        return l;
    }
};