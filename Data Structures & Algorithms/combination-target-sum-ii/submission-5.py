class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        curr_sol = []
        candidates.sort()

        def dfs(i, delta):
            if delta == 0:
                sol.append(list(curr_sol))
                return

            if i == len(candidates) or delta < 0:
                return

            curr_sol.append(candidates[i])
            dfs(i + 1, delta - candidates[i])

            curr_sol.pop()
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            i = j
            dfs(i, delta)

        dfs(0, target)
        return sol