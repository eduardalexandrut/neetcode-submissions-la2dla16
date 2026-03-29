class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        sol = []
        curr_sol = []
        visited = set()

        def back():
            if len(curr_sol) == len(nums):
                sol.append(curr_sol[:])
                return

            for num in nums:
                if num not in visited:
                    # 1. Action: Choose the number
                    curr_sol.append(num)
                    visited.add(num)

                    # 2. Recurse to go deeper
                    back()

                    # 3. Backtrack: Undo the choice so we can try a different number in this slot
                    visited.remove(num)
                    curr_sol.pop()

        
        back()
        return sol