class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        sol = []
        curr_sol = []

        def dfs(numOpen, numClosed):
        
            if len(curr_sol) == 2*n:
                sol.append("".join(curr_sol))
                return
            
            if numOpen < n:
                curr_sol.append("(")
                dfs(numOpen + 1, numClosed)
                curr_sol.pop()

            if numClosed < numOpen:
                curr_sol.append(")")
                dfs(numOpen, numClosed + 1)
                curr_sol.pop()


        dfs(0,0)
        return sol