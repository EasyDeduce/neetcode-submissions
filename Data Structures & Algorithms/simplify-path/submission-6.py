class Solution:
    def simplifyPath(self, path: str) -> str:
        dir=[]
        i=0
        while i<len(path):
            if path[i]=="/":
                tdir=""
                while i<len(path):
                    if i+3<len(path) and (path[i:i+4]=="/../"):
                        if len(dir)>0:
                            dir.pop()
                        i+=3
                    elif i+2==len(path)-1 and path[i:i+3]=="/..":
                        if len(dir)>0:
                            dir.pop() 
                        i+=3
                    elif i+1==len(path)-1 and path[i:i+2]=="/.":
                        i+=2
                    elif i+2<len(path) and path[i:i+3]=="/./":
                        i+=2
                    elif path[i]=="/" :
                        i+=1
                    else:
                        while i<len(path):
                            if path[i]=="/":
                                break
                            tdir+=path[i]
                            i+=1
                        dir.append(tdir)
                        tdir=""
        s="/"
        for i in range(len(dir)):
            s+=dir[i]
            if i!=len(dir)-1:
                s+="/"
        return s
        
                