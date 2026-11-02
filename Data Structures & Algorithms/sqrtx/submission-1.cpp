class Solution {
public:
    int mySqrt(int x) {
        if (x==0){
            return 0;
        }
        int i=1;
        while (i<=x){
            if ((long long)i*i>x){
                break;
            }
            i+=1;
        }
        return (i-1);
    }
};