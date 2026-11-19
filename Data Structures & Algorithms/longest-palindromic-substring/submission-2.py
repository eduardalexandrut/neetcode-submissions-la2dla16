class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resIndex = 0

        for i in range(len(s)):
            # Even
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = (r - l + 1)
                    resIndex = l
                l -= 1
                r += 1

            # Odd
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = (r - l + 1)
                    resIndex = l
                l -= 1
                r += 1
        
        return s[resIndex:resIndex + resLen]