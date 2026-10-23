class Solution {
public:
    string addBinary(string a, string b) {
        int i=a.length()-1;
        int j=b.size()-1;
        int len=max(i,j);
        if (a.size()<b.size()){
            a.insert(0,b.size()-a.size(),'0');
        }
        else if (b.size()<a.size()){
            b.insert(0,a.size()-b.size(),'0');
        }
        int carry=0;
        string res="";
        while (len>=0){
            if (a[len]=='1'){
                if (b[len]=='0'){
                    if (carry==0){
                        res+='1';
                        carry=0;
                    }
                    else{
                        res+='0';
                        carry=1;
                    }
                }
                else{
                    if (carry==0){
                        res+='0';
                        carry=1;
                    }
                    else{
                        res+='1';
                        carry=1;
                    }
                }
            }
            else{
                if (b[len]=='0'){
                    if (carry==0){
                        res+='0';
                        carry=0;
                    }
                    else{
                        res+='1';
                        carry=0;
                    }

                }
                else{
                    if (carry==0){
                        res+='1';
                        carry=0;
                    }
                    else{
                        res+='0';
                        carry=1;
                    }
                }
            }
            len-=1;
        }
        if (carry==1){
            res+='1';
        }
        reverse(res.begin(), res.end());
        return res;
    }
};