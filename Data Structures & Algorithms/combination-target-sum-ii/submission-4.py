class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sol = []
        curr_sol = []

        def dfs(i, delta):
            if delta == 0:
                sol.append(list(curr_sol))
                return

            if i >= len(candidates) or delta < 0:
                return

            curr_sol.append(candidates[i])
            dfs(i + 1, delta - candidates[i])
            curr_sol.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, delta)

        dfs(0, target)
        return sol