class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resStartIndex = 0

        # Even palindrome
        for i in range(len(s)):
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resStartIndex =  l
                l -= 1
                r += 1


        # Odd palindrome
        for i in range(len(s)):
            l = i
            r = i + 1
        
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resStartIndex =  l
                l -= 1
                r += 1


        return s[resStartIndex: resStartIndex + resLen]