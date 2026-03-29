class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        curr_sol = []

        def back(open_, closed):
            if len(curr_sol) == 2 * n:
                sol.append("".join(curr_sol))
                return
            
            if open_ < n:
                curr_sol.append("(")
                back(open_ + 1, closed)
                curr_sol.pop()    
            
            if closed < open_:
                curr_sol.append(")")
                back(open_, closed + 1)
                curr_sol.pop()

        back(0, 0)

        return sol