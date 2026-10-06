class Solution:

    def encode(self, strs: List[str]) -> str:
        r=[]
        for s in strs:
            # print(s)
            for c in s:
                r.append(chr(((ord(c)-ord('a')-1))+ord('a')))
                # print(c,r[-1])
            r.append("₹")
        return "".join(r) 
    def decode(self, s: str) -> List[str]:
        r=[]
        i=0
        # print(s)
        while i<len(s):
            t=""
            while s[i]!="₹":
                t+=chr(((ord(s[i])-ord('a')+1))+ord('a'))
                i+=1
            i+=1
            r.append(t)
        return r