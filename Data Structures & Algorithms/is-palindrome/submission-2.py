class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
       
        string = "".join(char for char in s if char.isalnum() or char.isspace())
        string = "".join(string.split())
        string = string.lower()
        l = 0
        r = len(string) - 1
        print(string)
        while (l < r):
            if (string[l] != string[r]):
                return False
            l+=1
            r-=1
        return True