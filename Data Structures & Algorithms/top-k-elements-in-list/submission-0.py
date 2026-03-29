class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_map = {}

        for num in nums:
            if num not in dict_map:
                dict_map[num] = []
            dict_map[num].append(num)
        sorted_items = sorted(dict_map.items(), key=lambda item: len(item[1]), reverse=True)
    
        # Extract the top k keys
        top_k_keys = [key for key, _ in sorted_items[:k]]
    
        return top_k_keys