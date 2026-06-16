class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
 
        l = 0
        seen_set = set()
        sol = 0

        for r in range(len(s)):
            while s[r] in seen_set:
                seen_set.remove(s[l])
                l += 1
            seen_set.add(s[r])
            sol = max(sol, r - l + 1)

        return sol