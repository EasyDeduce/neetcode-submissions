class Solution {
public:
    long long minEnd(int n, int x) {
        long long res =x;
        while (n-1>0){
            res+=1;
            res = res | x;
            n-=1;
        }
        return res;
    }
};