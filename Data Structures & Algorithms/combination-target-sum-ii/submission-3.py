class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sol = []
        curr_sol = []

        def backtracking(i, curr_sum):

            if curr_sum == target:
                sol.append(curr_sol[:])
                return

            if curr_sum > target or i >= len(candidates):
                return

            # Include step
            curr_sol.append(candidates[i])
            backtracking(i + 1, curr_sum + candidates[i])

            # Exclude step
            curr_sol.pop()

            # Skip duplicate numbers
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtracking(i + 1, curr_sum)

        backtracking(0, 0)
        return sol