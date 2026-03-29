class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol = []
        curr_sol = []

        # Checks if a string is palindrome(smae forward and backward)
        def isPalindrome(word):
            return word == word[::-1]

        def backtrack(i):
            if i >= len(s):
                sol.append(curr_sol[:])
                return

            for j in range(i, len(s)):
                substring = s[i : j + 1]

                if isPalindrome(substring):
                    curr_sol.append(substring)
                    backtrack(j + 1)
                    curr_sol.pop()
        backtrack(0)
        return sol
        