class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        m={"R": "Radiant", "D":"Dire"}
        x=0
        vis=[0]*len(senate)
        while True:
            if vis[x%len(senate)]==0:
                c=senate[x%len(senate)]
                r=x+1
                while r%len(senate)!=x%len(senate):
                    if (senate[r%len(senate)]!=c and vis[r%len(senate)]==0):
                        vis[(r)%len(senate)]=1
                        break
                    r+=1
                if r%len(senate)==x%len(senate):
                    return m[senate[x%len(senate)]]                    
            x+=1
        return "Dire"