class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minc=99999999999
        for i in range(0,len(blocks)-k+1):
            tc=0
            for j in range(i,i+k):
                if blocks[j]=="W":
                    tc+=1
            if tc<minc:
                minc=tc
        return minc