class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inc= defaultdict(int)
        out= defaultdict(int)
        for i in range(1,n+1):
            inc[i]=0
            out[i]=0
        for i,j in trust:
            inc[j]+=1
            out[i]+=1
        print(inc, out)
        for i in range(1,n+1):
            if (inc[i]==n-1 and out[i]==0):
                return i
        return -1