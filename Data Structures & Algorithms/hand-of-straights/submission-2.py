class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
       
        if len(hand) % groupSize:
            return False
        
        frequencyMap = dict()

        for num in hand:
            frequencyMap[num] = frequencyMap.get(num, 0) + 1

        hand.sort()
        for num in hand:
            if frequencyMap[num]:
                for i in range(num, num + groupSize):
                    if frequencyMap.get(i, 0) == 0:
                        return False
                    frequencyMap[i] -= 1

        return True

