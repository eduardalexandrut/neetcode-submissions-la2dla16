from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)  # Frequency of characters in s1
        window_count = Counter()  # Frequency of current window in s2
        
        l = 0
        for r in range(len(s2)):
            # Add the current character to the window count
            window_count[s2[r]] += 1
            
            # Ensure window size matches the size of s1
            if r - l + 1 > len(s1):
                # Remove the leftmost character from the window
                if window_count[s2[l]] == 1:
                    del window_count[s2[l]]
                else:
                    window_count[s2[l]] -= 1
                l += 1
            
            # If the current window matches the frequency of s1, we have a permutation
            if window_count == s1_count:
                return True
        
        return False
