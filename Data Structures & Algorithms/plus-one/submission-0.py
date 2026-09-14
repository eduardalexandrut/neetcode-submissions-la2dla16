class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for d in digits:
            string += str(d)

        incremented = int(string) + 1
        strInc = str(incremented)
        return [int(s) for s in strInc]