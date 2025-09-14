from collections import Counter
class Solution():
    def topKFrequent(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        top_k_frequent = sorted(freq.keys(), key=freq.get, reverse=True)[:k]
        return top_k_frequent