from collections import Counter
class Solution:
    def cmp(self, ci:int, si:int, mi1:int, mi2:int)-> (int,int):
        if mi2-mi1>ci-si:
            return (si,ci)
        return (mi1,mi2)
    def cmpfreq(self, map:Counter(), map2:Counter())-> bool:
        for key in map:
            if (map[key]>map2[key]):
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        if (len(s)<len(t)):
             return ""
        soi=set()
        reqmap= Counter(t)
        for c in t:
            soi.add(c)
        list= [(i,c) for i, c in enumerate(s) if c in soi]
        if not list:
            return ""
        if t in s:
            return t
        mi1,mi2= (0,1001)
        ts=set()
        it=0
        map= Counter()
        (si,sc)=list[it]
        it+=1                                                                                                                                                                                                                                                                                                                             
        max_count=len(soi)
        ts.add(sc)
        if (len(ts)==max_count):
            return sc
        map[sc]+=1
        print(reqmap, map)
        for r in range(1,len(list)):
            (ci,cc)= list[r]
            map[cc]+=1
            ts.add(cc)
            if (len(ts)==max_count and self.cmpfreq(reqmap,map)):
                mi1,mi2= self.cmp(ci,si,mi1,mi2)
                map[sc]-=1
                if map[sc]==0:
                    ts.remove(sc)
                (si,sc)=list[it]
                it+=1
                ts.add(sc)
                while (len(ts)==max_count and self.cmpfreq(reqmap,map)):
                    mi1,mi2= self.cmp(ci,si,mi1,mi2)
                    map[sc]-=1
                    if (map[sc]==0):
                        ts.remove(sc)
                    si,sc=list[it]
                    it+=1
                    ts.add(sc)
        if (mi2==1001):
            return ""
        return s[mi1:mi2+1]   
                







        