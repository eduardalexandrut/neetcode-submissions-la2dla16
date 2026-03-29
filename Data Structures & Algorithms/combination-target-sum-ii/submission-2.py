class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(start, current, total):
            if total == target:
                res.append(current[:])
                return
            
            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                backtrack(i + 1, current, sum(current))
                current.pop()

        
        res = []
        candidates.sort()
        backtrack(0, [], 0)
        return res