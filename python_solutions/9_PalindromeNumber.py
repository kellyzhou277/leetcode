#check if an integer is a palindrome

class Solution():
    def isPalindrome(self,num):
        #use two points to check
        num_str = str(num)
        i = 0
        j = len(num_str) - 1
        while i < j:
            if num_str[i] != num_str[j]:
                return False
            i += 1
            j -= 1
        return True

def test_solution():
    solution = Solution()
    num1 = 121
    print(f"Test 1: {solution.isPalindrome(num1)}")
    num2 = 1332
    print(f"Test 2: {solution.isPalindrome(num2)}")
if __name__ == "__main__":
    test_solution()