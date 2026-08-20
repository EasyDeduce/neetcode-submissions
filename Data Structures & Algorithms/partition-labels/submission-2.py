class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mi={}
        t=[]
        for i in range(len(s)):
            mi[s[i]]=max(mi.get(s[i],0),i)
        vis=set()
        for i in range(len(s)):
            if s[i] not in vis:
                vis.add(s[i])
                m=mi.get(s[i])-i
                j=i
                while j<(m+i):
                    if (s[j] not in vis) and (s[j]!=s[i]):
                        vis.add(s[j])
                        m=max(m,mi.get(s[j])-i)
                    j+=1
                t.append(m+1)
        return t

                