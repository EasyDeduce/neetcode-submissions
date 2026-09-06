class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        boats=0
        r= len(people)-1
        while l<=r:
            if (people[l]==limit):
                l+=1
                boats+=1
                continue
            if (people[r]==limit):
                r-=1
                boats+=1
                continue
            if (people[l]+people[r]<=limit):
                l+=1
                r-=1
                boats+=1
                continue
            else:
                boats+=1
                r-=1
        return boats

