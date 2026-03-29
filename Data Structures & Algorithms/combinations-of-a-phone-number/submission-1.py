class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
            
        sol = []
        curr_sol = []

        # 1. Map digits to letters
        digit_to_letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(i):
            if len(curr_sol) == len(digits):
                sol.append("".join(curr_sol))
                return

            available_digits = digit_to_letters[digits[i]]

            for c in available_digits:
                curr_sol.append(c)
                backtrack(i + 1)
                curr_sol.pop()
            
        backtrack(0)
        return sol