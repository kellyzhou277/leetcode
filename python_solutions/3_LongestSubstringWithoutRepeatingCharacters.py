#find the length of the longest substring without repeating characters
#2 pointers maybe, if there's a repeating character, we will restart
class Solution():
    def lengthOfLongestSubstring(self, s):
        #we will use a sliding window and a set
        left = max_length = 0
        char_set = set()
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
    
def test_solution():
    solution = Solution()
    s1 = "abcabcbb"
    print(f"Test 1: {solution.lengthOfLongestSubstring(s1)}")
    s2 = "bbbbbbbb"
    print(f"Test 2: {solution.lengthOfLongestSubstring(s2)}")

if __name__ == "__main__":
    test_solution()