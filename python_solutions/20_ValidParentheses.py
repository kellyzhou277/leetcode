#check if the parantheses are valid

class Solution():
    def isValid(self, s: str) -> bool:
        stack = []
        hashm = {')':'(', ']':'[', '}' :'{'}
        for element in s:
            if (stack and element in hashm and stack[-1] == hashm[element]):
                stack.pop()
            else:
                stack.append(element)
        return not stack
    
def test_solution():
    solution = Solution()
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    print(f"Test 1: {solution.isValid(s1)}")
    print(f"Test 2: {solution.isValid(s2)}")
    print(f"Test 3: {solution.isValid(s3)}")

if __name__ == "__main__":
    test_solution()
