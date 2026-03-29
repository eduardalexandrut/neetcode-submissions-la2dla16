class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for s in strs:
            # Sort the characters in the string and use the sorted string as a key
            sorted_str = ''.join(sorted(s))
            if sorted_str not in anagrams:
                anagrams[sorted_str] = []
            anagrams[sorted_str].append(s)
        return list(anagrams.values())
        

                