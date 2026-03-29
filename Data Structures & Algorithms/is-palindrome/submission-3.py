class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        betterS = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        l = 0
        r = len(betterS) - 1

        while l < r:
            if betterS[l] != betterS[r]:
                return False
            l +=1
            r -=1
        return True
