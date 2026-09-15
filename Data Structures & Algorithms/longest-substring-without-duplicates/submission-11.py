class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        i=0
        j=0
        maxlen=0
        t=set()
        matching=0
        while j<len(s):
            if s[j] not in t:
                t.add(s[j])
                if j==len(s)-1:
                    return max(maxlen, j-i+1)
                # print("adding ", s[j], i,j)
                j+=1
                continue
            # matching+=1
            maxlen= max(maxlen, j-i)
            # print(s[i:j+1], j-i)
            while i<len(s) and s[i]!=s[j]:
                t.remove(s[i])
                i+=1
            i+=1
            j+=1
        # if matching==0:
        #     return len(s)
        return maxlen