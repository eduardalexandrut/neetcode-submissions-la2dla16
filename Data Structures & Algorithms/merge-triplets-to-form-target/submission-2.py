class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        match_x = False
        match_y = False
        match_z = False

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            if t[0] == target[0]:
                match_x = True
            if t[1] == target[1]:
                match_y = True
            if t[2] == target[2]:
                match_z = True

            if match_x and match_y and match_z:
                return True
        
        return match_x and match_y and match_z