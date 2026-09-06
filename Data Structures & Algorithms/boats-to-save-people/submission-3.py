class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        boats=0
        r= len(people)-1
        # print(people)
        while l<=r:
            if (people[l]==limit):
                # print("here1")
                l+=1
                boats+=1
                continue
            if (people[r]==limit):
                # print("here2")
                r-=1
                boats+=1
                continue
            if (people[l]+people[r]<=limit):
                # print("here3")
                l+=1
                r-=1
                boats+=1
                continue
            else:
                # print("here4")
                boats+=1
                r-=1
        return boats

