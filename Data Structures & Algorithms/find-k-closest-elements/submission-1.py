class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr=list(map(lambda val: val-x,arr))
        t=[]
        m=-1000000
        mi=-1
        for i in range(len(arr)):
            if (abs(arr[i])<abs(m)):
                m=arr[i]
                mi=i
        left=mi-1
        right=mi+1
        t.append(arr[mi]+x)
        k-=1
        while(left>=0 and right<len(arr) and k>0):
            if abs(arr[left])<=abs(arr[right]):
                t.append(arr[left]+x)
                left-=1
                k-=1
            else:
                t.append(arr[right]+x)
                right+=1
                k-=1
        while (left>=0 and k>0):
            t.append(arr[left]+x)
            left-=1
            k-=1
        while (right<len(arr) and k>0):
            t.append(arr[right]+x)
            right+=1
            k-=1
        t.sort()
        return t