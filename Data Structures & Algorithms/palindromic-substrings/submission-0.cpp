class Solution {
public:
    int countSubstrings(string s) {
        int count =0;
        for (int i=0; i<s.size(); i++){
            // odd
            int l=i;
            int r=i;
            while (l>=0 && r<s.size() && s[l]==s[r]){
                    l-=1;
                    r+=1;
                    count+=1;
            }
            //even
            l=i;
            r=i+1;
            while (l>=0 && r<s.size() && s[l]==s[r]){
                    l-=1;
                    r+=1;
                    count+=1;
            }
        }
        return count;
    }
};
