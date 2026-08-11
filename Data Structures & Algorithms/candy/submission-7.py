from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        tot = 0
        curr=0
        i = 0
        ones=0
        if (len(ratings)==1): return 1
        while i < len(ratings)-1:
            t = 0
            print(ratings[i], ratings[i+1], tot)
            if ratings[i] < ratings[i + 1]:
                while i < len(ratings) - 1 and ratings[i] < ratings[i + 1]:
                    t += 1
                    i += 1
                t+=1
                tot +=((t*(t+1))//2)-curr
                curr=t

            elif ratings[i]==ratings[i+1]:
                j=i
                while j<len(ratings)-1 and ratings[j]==ratings[j+1]:
                    ones+=1
                    j+=1
                curr=1
                tot+=ones
                ones=0
                if (i==0):
                    tot+=1
                i=j

            else:
                while i < len(ratings)-1 and ratings[i] > ratings[i + 1]:
                    t += 1
                    i += 1  
                t+=1
                if (t>=curr):
                    tot+=((t*(t+1))//2)-curr
                    curr=1
                else:
                    tot+=(t*(t-1))//2
                    curr=1
        return tot