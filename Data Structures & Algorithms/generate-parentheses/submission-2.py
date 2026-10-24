class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        sol = []
        curr_sol = []

        def dfs(i, open_count, closed_count):
            if i >= 2*n:
                sol.append("".join(curr_sol))
                return

            if open_count > closed_count:
                curr_sol.append(")")
                dfs(i + 1, open_count, closed_count + 1)
                curr_sol.pop()
            if open_count < n:
                curr_sol.append("(")
                dfs(i + 1, open_count + 1, closed_count)
                curr_sol.pop()
            return

        dfs(0, 0, 0)
        return sol