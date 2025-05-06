class Solution():
    def romanToInt(self, s):
        value_hash = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s) - 1):
            #since the digit should be decreasing, if the digit increases, that means
            #we have a case like IV or XL, in which case we subtract first roman digit
            #from second roman digit
            if value_hash[s[i]] < value_hash[s[i+1]]:
                ans = ans - value_hash[s[i]]
            #otherwise, we add it to the number
            else:
                ans = ans + value_hash[s[i]]
        #add the last digit
        return ans + value_hash[s[-1]]
def test_solution():
    solution = Solution()
    s1 = "III"
    print(f"Test 1: {solution.romanToInt(s1)}")
    s2 = "LVIII"
    print(f"Test 2: {solution.romanToInt(s2)}")

if __name__ == "__main__":
    test_solution()