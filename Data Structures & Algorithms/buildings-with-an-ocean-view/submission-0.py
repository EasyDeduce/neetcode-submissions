class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        t=[0]
        for i in range(1,len(heights)):
            if heights[i]>=heights[t[-1]]:
                while len(t)>0 and heights[i]>=heights[t[-1]]:
                    t.pop()
                t.append(i)
            else:
                t.append(i)
        return t
        