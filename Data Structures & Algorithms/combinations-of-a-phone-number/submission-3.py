class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []

        sol = []
        curr_sol = []

        digitToLetter = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":[ "t", "u", "v"],
            "9":["w", "x", "y", "z"]
        }

        def dfs(i):
            if  i == len(digits):
                sol.append("".join(curr_sol))
                return

            for c in digitToLetter[digits[i]]:
                curr_sol.append(c)
                dfs(i + 1)
                curr_sol.pop()


        dfs(0)
        return sol