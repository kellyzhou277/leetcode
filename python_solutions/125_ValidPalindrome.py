class Solution():
    def validPalindrome(self, s: str) -> bool:
        clean_string = "".join(e for e in s if e.isalnum()).lower()
        left = 0
        right = len(clean_string) -1
        while left < right:
            if clean_string[left] != clean_string[right]:
                return False
            left += 1
            right -= 1
        return True


