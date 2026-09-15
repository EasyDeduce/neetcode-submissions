class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        maxlen=0
        t=set()
        while j<len(s):
            if s[j] not in t:
                t.add(s[j])
                if j==len(s)-1:
                    return max(maxlen, j-i+1)
                j+=1
                continue
            maxlen= max(maxlen, j-i)
            while i<len(s) and s[i]!=s[j]:
                t.remove(s[i])
                i+=1
            i+=1
            j+=1
        return maxlen