class Solution:
    x=0
    def validPalindrome(self, s: str) -> bool:
        i=0
        while (i<int(len(s)/2)):
            if (self.x==0 and s[i]!=s[len(s)-1-i]):
                self.x+=1
                if i==0:
                    return (self.validPalindrome(s[1:]) or self.validPalindrome(s[:len(s)-1]))
                return (self.validPalindrome(s[:i]+s[i+1:]) or self.validPalindrome(s[:len(s)-1-i]+s[len(s)-i:]))
            if (self.x>0 and s[i]!=s[len(s)-1-i]):
                return False
            i+=1
        return True