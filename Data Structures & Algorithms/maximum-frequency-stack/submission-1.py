class FreqStack:
    def __init__(self):
        self.smap={}
        self.stack=[]
    def push(self,val:int)->None:
        self.smap[val]=self.smap.get(val,0)+1
        self.stack.append(val)
    def pop(self)->int:
        maxf=0
        maxi=0
        k=len(self.stack)-1
        while k>=0:
            if self.smap[self.stack[k]]>maxf:
                maxf=self.smap[self.stack[k]]
                maxi=k
            k-=1
        maxn=self.stack[maxi]
        self.stack.pop(maxi)
        self.smap[maxn]-=1
        return maxn