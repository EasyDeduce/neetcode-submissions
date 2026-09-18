class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        s=""
        while i<len(word1) and i<len(word2):
            s+=word1[i]
            s+=word2[i]
            i+=1
        j=i
        while j<len(word2):
            s+=word2[j]
            j+=1
        j=i
        while j<len(word1):
            s+=word1[j]
            j+=1
        return s
