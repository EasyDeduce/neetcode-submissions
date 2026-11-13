class Solution {
public:
    long long minEnd(int n, int x) {
        long long res =x;
        int bit_count =0;
        n= n-1;
        while (n>0){
            if ((x&1) == 0){
                if ( (n & 1) == 1){
                    res = res | 1LL<<bit_count;
                }
                n = n>>1;
            }
            bit_count+=1;
            x= x>>1;
        }
        return res;
    }
};