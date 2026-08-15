class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minc =k
        l=0
        r=0
        cw=0
        while l==0 and r<k:
            if blocks[r]=="W":
                cw+=1
            r+=1
        if cw<minc:
            minc=cw
        while r<len(blocks)-1:
            if blocks[l]=="B" and blocks[r]=="W" :
                cw+=1
            elif blocks[l]=="W" and blocks[r]=="B" :
                cw-=1
            print(cw)
            if cw<minc:
                minc=cw
            r+=1
            l+=1
        return minc