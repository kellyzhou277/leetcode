from collections import defaultdict
class Solution:
    def groupAnagram(self, strs: list[str]) -> list[list[str]]:
        anagram_list = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            anagram_list[sorted_s].append(s)
        return list(anagram_list.values())
