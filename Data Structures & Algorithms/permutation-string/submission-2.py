from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        window_count = Counter()
        l = 0

        for r in range(len(s2)):
            window_count[s2[r]] += 1#Adds the new char to the counter or inceases its frequency i
            if r - l + 1 > len(s1):
                if window_count[s2[l]] == 1:
                    del window_count[s2[l]]
                else:
                    window_count[s2[l]] -= 1
                l += 1

            #Check for a match
            if window_count == s1_count:
                return True
        return False