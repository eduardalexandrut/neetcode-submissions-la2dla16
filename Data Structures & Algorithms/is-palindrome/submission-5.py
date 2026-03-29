class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        modified_s = re.sub(r'[^a-zA-Z0-9]','',s).lower()

        l = 0
        r = len(modified_s) - 1

        while l < r:
            if modified_s[l] != modified_s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True