class Solution:
    def validAnagram(self, s: str, t: str) -> bool:
        #method 1
        if len(s) != len(t):
            return False
        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
        for s in s_dict.keys():
            if s not in t_dict.keys() or s_dict[s] != t_dict[s]:
                return False
        return True
        #method 2
        if len(s) != len(t):
            return False
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        for i in range(len(s_sorted)):
            if s_sorted[i] != t_sorted[i]:
                return False
        return True
        #method 3:
        return True if Counter(s) == Counter(t) else False