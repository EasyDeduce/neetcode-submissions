class Solution:
    def numDecodings(self, s: str) -> int:
        dp1 = 1
        dp2 =0
        for i in range(len(s)-1, -1, -1):
            current =0 
            if s[i]=="0":
                current =0 
            else:
                current = dp1
            
            if (i+1<len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456"))):
                current += dp2
            
            dp2= dp1
            dp1 = current

        return dp1
