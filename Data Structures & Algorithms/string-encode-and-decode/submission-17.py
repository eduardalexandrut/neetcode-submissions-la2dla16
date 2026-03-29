class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + '#' + s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        
        while i < len(s):#loop up to the end of the string s
            j = i
            while s[j] != '#':#loop until you find the char '#' and count how many chars the next word has
                j += 1
            length = int(s[i:j]) #find the lenth of the word 
            i = j + 1
            j = i + length
            ans.append(s[i:j])
            i = j
        return ans